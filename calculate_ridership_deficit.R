library(tidyverse)

# 1. Load All Datasets
message("Loading multi-variable datasets...")

# Commuting & Ridership
b08301 <- read_delim("Transit_Fragmentation_Research/raw_census/B08301_expanded.dat", 
                    delim = "|", col_names = FALSE, show_col_types = FALSE) %>%
  select(GEOID = X1, Total_Workers = X2, Transit_Workers = X20)

# Median Income
b19013 <- read_delim("Transit_Fragmentation_Research/raw_census/B19013_expanded.dat", 
                    delim = "|", col_names = FALSE, show_col_types = FALSE) %>%
  select(GEOID = X1, Median_Income = X2)

# Total Population
b01003 <- read_delim("Transit_Fragmentation_Research/raw_census/B01003_expanded.dat", 
                    delim = "|", col_names = FALSE, show_col_types = FALSE) %>%
  select(GEOID = X1, Population = X2)

# Housing Units (Density Proxy)
b25001 <- read_delim("Transit_Fragmentation_Research/raw_census/B25001_expanded.dat", 
                    delim = "|", col_names = FALSE, show_col_types = FALSE) %>%
  select(GEOID = X1, Housing_Units = X2)

# Land Area (Tract Gazetteer)
gazetteer <- read_tsv("Transit_Fragmentation_Research/data/2022_Gaz_tracts_national.txt", 
                     show_col_types = FALSE) %>%
  select(GEOID, Land_Area_SqMi = ALAND_SQMI) %>%
  mutate(GEOID = paste0("1400000US", GEOID))

# Combine All
df <- b08301 %>%
  left_join(b19013, by = "GEOID") %>%
  left_join(b01003, by = "GEOID") %>%
  left_join(b25001, by = "GEOID") %>%
  left_join(gazetteer, by = "GEOID") %>%
  mutate(across(c(Median_Income, Total_Workers, Transit_Workers, Population, Housing_Units, Land_Area_SqMi), as.numeric)) %>%
  filter(!is.na(Median_Income), Median_Income > 0, Total_Workers > 0, Land_Area_SqMi > 0) %>%
  mutate(
    Transit_Rate = Transit_Workers / Total_Workers,
    Pop_Density = Population / Land_Area_SqMi,
    Housing_Density = Housing_Units / Land_Area_SqMi
  )

# 2. Assign Regions and Status (Primary vs Secondary)
df <- df %>%
  mutate(
    Region = case_when(
      str_detect(GEOID, "US(39061|21117|21037|21015)") ~ "Cincinnati",
      str_detect(GEOID, "US(53033|53053|53061)") ~ "Seattle",
      str_detect(GEOID, "US(04013|04021)") ~ "Phoenix",
      str_detect(GEOID, "US(06075|06001|06013|06081|06041)") ~ "San Francisco",
      str_detect(GEOID, "US(26163|26125|26099)") ~ "Detroit",
      str_detect(GEOID, "US(12057|12103)") ~ "Tampa",
      str_detect(GEOID, "US(37183|37063)") ~ "Durham/Raleigh",
      str_detect(GEOID, "US(09001|09009)") ~ "Bridgeport/New Haven",
      str_detect(GEOID, "US(06065|06071)") ~ "Riverside",
      TRUE ~ "Other"
    ),
    Status = case_when(
      str_detect(GEOID, "US(39061|53033|04013|06075|26163|12057|37183|09001|06065)") ~ "Primary",
      TRUE ~ "Secondary"
    )
  ) %>%
  filter(Region != "Other")

# 3. Refined Counterfactual Model (Bias Correction)
# We control for:
# - log(Income): The wealth effect on car ownership
# - log(Pop_Density): The built environment / land use bias
# - log(Housing_Density): Urban form / multifamily proxy
# - Region: Region-specific fixed effects (Cincy markets vs Seattle markets)
message("Building refined counterfactual model with density controls...")
model_refined <- lm(Transit_Rate ~ log(Median_Income) + log(Pop_Density + 1) + log(Housing_Density + 1) + Region, 
                   data = df %>% filter(Status == "Primary"))

summary(model_refined)

# 4. Predict Deficits for Secondary areas (using the refined comparable core)
df_secondary <- df %>% filter(Status == "Secondary")
df_secondary$Predicted_Rate <- predict(model_refined, newdata = df_secondary)
df_secondary$Predicted_Rate <- pmax(0, df_secondary$Predicted_Rate)

df_secondary <- df_secondary %>%
  mutate(
    Missing_Riders = (Predicted_Rate - Transit_Rate) * Total_Workers
  )

# 5. Aggregate
summary_deficit <- df_secondary %>%
  group_by(Region) %>%
  summarise(
    Actual_Riders = sum(Transit_Workers),
    Predicted_Potential = sum(Predicted_Rate * Total_Workers),
    Ridership_Deficit = sum(Missing_Riders),
    Pct_Market_Loss = Ridership_Deficit / Predicted_Potential,
    Tract_Count = n(),
    .groups = "drop"
  ) %>%
  arrange(desc(Pct_Market_Loss))

# 6. Save
write_csv(summary_deficit, "Transit_Fragmentation_Research/ridership_deficit_summary.csv")
write_csv(df_secondary, "Transit_Fragmentation_Research/tract_deficit_results.csv")

message("\nRefined Ridership Deficit Analysis Complete (Bias Corrected):")
print(summary_deficit)
