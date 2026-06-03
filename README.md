# Transit Fragmentation Research: Quantifying Governance Friction

## Overview
This project introduces the **Transit Fragmentation Index (TFI)**, a metric derived from the inverse of a ridership-based Herfindahl-Hirschman Index (HHI), to quantify institutional "friction" in US metropolitan transit systems. Using 2023 National Transit Database (NTD) data, the research analyzes how partitioning service among multiple independent authorities suppresses regional ridership.

## Key Data Science Skills
*   **Metric Development:** Designing the TFI to quantify abstract governance concepts.
*   **Data Wrangling:** Processing complex Federal Funding Allocation (FFA) datasets from the NTD.
*   **Comparative Analysis:** Benchmarking fragmentation across 480+ Urbanized Areas (UZAs).
*   **Economic Modeling:** Applying the Coase Theorem to institutional service delivery.

## Tech Stack
*   **R & Python:** Data processing and statistical analysis.
*   **Quarto:** Reproducible research and report generation.
*   **NTD API/Data:** Working with specialized federal transit datasets.

## Key Findings
*   Highly fragmented regions (e.g., San Francisco Bay Area, TFI: 17.0) exhibit significantly higher friction than consolidated regions (e.g., New York, TFI: 6.7), regardless of the raw number of agencies.
*   Fragmentation acts as a "transaction cost" for riders, creating a quantifiable penalty on per-capita ridership.

## Data Sources
*   **National Transit Database (NTD):** [2023 Annual Database Federal Funding Allocation](https://www.transit.dot.gov/ntd/data-product/2023-annual-database-federal-funding-allocation)
*   **US Census Bureau:** [American Community Survey (ACS) 5-Year Estimates](https://data.census.gov/)

## Structure
*   `analyze_fragmentation.py/R`: Core analytical scripts.
*   `TRANSIT_FRAGMENTATION_PAPER.qmd`: The primary research paper.
*   `DEFICIT_MAP.html`: Interactive visualization of ridership deficits.
