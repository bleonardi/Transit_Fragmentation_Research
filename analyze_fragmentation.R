library(tidyverse)
library(readxl)
library(httr)

# Configuration
data_dir <- "data"
ntd_csv_url <- "https://data.transportation.gov/api/views/5x22-djnv/rows.csv?accessType=DOWNLOAD"

dir.create(data_dir, showWarnings = FALSE)

download_file <- function(url, filename) {
  if (!file.exists(filename) || file.info(filename)$size < 1000) {
    message(paste("Downloading", filename, "..."))
    GET(url, write_disk(filename, overwrite = TRUE), 
        add_headers(`User-Agent` = "Mozilla/5.0"))
    message(paste("Successfully downloaded", filename))
  } else {
    message(paste(filename, "already exists and looks valid."))
  }
}

ntd_file <- file.path(data_dir, "ntd_2022_2024.csv")
download_file(ntd_csv_url, ntd_file)

# 1. Load NTD Data
message("Loading NTD data...")
df_ntd <- read_csv(ntd_file)

# 2. Process All Years and All UZAs
message("Calculating fragmentation metrics for all Urbanized Areas...")

# We aggregate across all years to get the total cumulative "Governance Friction"
df_metrics <- df_ntd %>%
  filter(!is.na(`Urbanized Area Name`)) %>%
  group_by(`Urbanized Area Code`, `Urbanized Area Name`) %>%
  summarise(
    Agency_Count = n_distinct(Agency),
    Total_UPT = sum(`Total Unlinked Passenger Trips`, na.rm = TRUE),
    Total_VRM = sum(`Total Actual Vehicle Revenue Miles`, na.rm = TRUE),
    .groups = "drop"
  ) %>%
  filter(Total_UPT > 0)

# To calculate HHI, we need the individual agency shares within each UZA
df_agency_shares <- df_ntd %>%
  filter(!is.na(`Urbanized Area Name`)) %>%
  group_by(`Urbanized Area Code`, Agency) %>%
  summarise(Agency_UPT = sum(`Total Unlinked Passenger Trips`, na.rm = TRUE), .groups = "drop")

# Join and calculate TFI
df_final_metrics <- df_agency_shares %>%
  inner_join(df_metrics %>% select(`Urbanized Area Code`, `Urbanized Area Name`, Total_UPT, Agency_Count), by = "Urbanized Area Code") %>%
  mutate(share_sq = (Agency_UPT / Total_UPT)^2) %>%
  group_by(`Urbanized Area Code`, `Urbanized Area Name`, Agency_Count, Total_UPT) %>%
  summarise(HHI = sum(share_sq), .groups = "drop") %>%
  mutate(Fragmentation_Index = 1 / HHI) %>%
  arrange(desc(Fragmentation_Index))

# 3. Save Results
write_csv(df_final_metrics, "transit_fragmentation_results.csv")
message("Full results saved to transit_fragmentation_results.csv")

# Print Top 20 Most Fragmented
print(head(df_final_metrics, 20))
