import requests
import pandas as pd
import numpy as np

# ACS Variables: 
# Total Workers: B08301_001E
# Public Transit: B08301_010E
# Median Income: B19013_001E
# Land Area: B01001_001E (Population) + we need land area from gazetteer or Tiger

VARIABLES = "NAME,B08301_001E,B08301_010E,B19013_001E"

def fetch_census_data(state, counties):
    # state is 2-digit FIPS, counties is list of 3-digit FIPS
    all_data = []
    for county in counties:
        url = f"https://api.census.gov/data/2022/acs/acs5?get={VARIABLES}&for=tract:*&in=state:{state}&in=county:{county}"
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            df = pd.DataFrame(data[1:], columns=data[0])
            all_data.append(df)
    return pd.concat(all_data) if all_data else pd.DataFrame()

# Cincinnati Region
# Ohio: Hamilton (061)
# Kentucky: Kenton (117), Campbell (037), Boone (015)
cincy_oh = fetch_census_data("39", ["061"])
cincy_ky = fetch_census_data("21", ["117", "037", "015"])

# Seattle Region
# King (033), Pierce (053), Snohomish (061)
seattle_p = fetch_census_data("53", ["033"])
seattle_s = fetch_census_data("53", ["053", "061"])

# Clean and combine
def clean_df(df, region_name, side):
    df = df.copy()
    df['region'] = region_name
    df['side'] = side
    cols = ['B08301_001E', 'B08301_010E', 'B19013_001E']
    for col in cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    df['transit_share'] = df['B08301_010E'] / df['B08301_001E']
    return df

df_cincy = pd.concat([clean_df(cincy_oh, "Cincinnati", "Primary"), clean_df(cincy_ky, "Cincinnati", "Secondary")])
df_seattle = pd.concat([clean_df(seattle_p, "Seattle", "Primary"), clean_df(seattle_s, "Seattle", "Secondary")])

full_df = pd.concat([df_cincy, df_seattle])
full_df.to_csv("Transit_Fragmentation_Research/ridership_deficit_data.csv", index=False)
print("Data fetched and saved.")
