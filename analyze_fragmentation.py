import pandas as pd
import requests
import os
import numpy as np

# Configuration
DATA_DIR = "data"
# Using the Socrata API CSV link which is more reliable for automation
NTD_CSV_URL = "https://data.transportation.gov/api/views/5x22-djnv/rows.csv?accessType=DOWNLOAD"
UA_CROSSWALK_URL = "https://www2.census.gov/geo/relfiles/cbsa23/ua20_cbsa23_natl.txt"

def download_file(url, filename):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    if not os.path.exists(filename) or os.path.getsize(filename) < 1000:
        print(f"Downloading {filename}...")
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"Successfully downloaded {filename}")
        else:
            print(f"Failed to download {filename}. Status code: {response.status_code}")
    else:
        print(f"{filename} already exists and looks valid.")

def main():
    os.makedirs(DATA_DIR, exist_ok=True)
    
    ntd_file = os.path.join(DATA_DIR, "ntd_2023_ffa.csv")
    crosswalk_file = os.path.join(DATA_DIR, "ua_cbsa_crosswalk.txt")
    
    download_file(NTD_CSV_URL, ntd_file)
    download_file(UA_CROSSWALK_URL, crosswalk_file)
    
    # 1. Load NTD Data
    print("Loading NTD data...")
    df_ntd = pd.read_csv(ntd_file)
    
    # Filter for 2023 if the file contains multiple years
    if 'Report Year' in df_ntd.columns:
        df_ntd = df_ntd[df_ntd['Report Year'] == 2023]
    
    print("Available columns:", df_ntd.columns.tolist())
    
    # Map columns based on standard Socrata field names for this dataset
    # Expected: 'Agency Name', 'UACE Code', 'UACE Name', 'Unlinked Passenger Trips', 'Vehicle Revenue Miles'
    # We'll use case-insensitive matching to be safe
    col_map = {}
    for target, patterns in {
        'Agency': ['Agency Name', 'Agency', 'Organization Name'],
        'UACE': ['UACE Code', 'UACE Number', 'Urbanized Area Code'],
        'UACE_Name': ['UACE Name', 'Urbanized Area Name'],
        'UPT': ['Unlinked Passenger Trips', 'UPT', 'Passenger Trips'],
        'VRM': ['Vehicle Revenue Miles', 'VRM', 'Revenue Miles']
    }.items():
        match = [c for c in df_ntd.columns if any(p.lower() in c.lower() for p in patterns)]
        if match:
            col_map[target] = match[0]
        else:
            print(f"Warning: Could not find column for {target}")

    if len(col_map) < 5:
        print("Required columns missing. Current map:", col_map)
        # Fallback to manual slice if we can't find them, but let's try to proceed
    
    df_clean = df_ntd[list(col_map.values())].copy()
    df_clean.columns = list(col_map.keys())
    
    # Ensure numeric types
    df_clean['UPT'] = pd.to_numeric(df_clean['UPT'], errors='coerce').fillna(0)
    df_clean['VRM'] = pd.to_numeric(df_clean['VRM'], errors='coerce').fillna(0)
    df_clean['UACE'] = pd.to_numeric(df_clean['UACE'], errors='coerce')
    
    # 2. Calculate Fragmentation Metrics per UACE
    print("Calculating fragmentation metrics...")
    
    uace_groups = df_clean.groupby('UACE')
    
    metrics = []
    for uace, group in uace_groups:
        if pd.isna(uace): continue
        
        total_upt = group['UPT'].sum()
        total_vrm = group['VRM'].sum()
        agency_count = group['Agency'].nunique()
        
        # HHI for UPT
        if total_upt > 0:
            upt_shares = group['UPT'] / total_upt
            hhi_upt = (upt_shares ** 2).sum()
        else:
            hhi_upt = np.nan
            
        # HHI for VRM
        if total_vrm > 0:
            vrm_shares = group['VRM'] / total_vrm
            hhi_vrm = (vrm_shares ** 2).sum()
        else:
            hhi_vrm = np.nan
            
        metrics.append({
            'UACE': uace,
            'UACE_Name': group['UACE_Name'].iloc[0] if 'UACE_Name' in group else f"UACE {uace}",
            'Agency_Count': agency_count,
            'HHI_UPT': hhi_upt,
            'HHI_VRM': hhi_vrm,
            'Total_UPT': total_upt,
            'Total_VRM': total_vrm
        })
        
    df_metrics = pd.DataFrame(metrics)
    df_metrics['Fragmentation_Index'] = 1 / df_metrics['HHI_UPT']
    
    # 3. Merge with Census Crosswalk
    print("Loading crosswalk...")
    try:
        # Some census files have footer or metadata lines that cause issues
        df_cw = pd.read_csv(crosswalk_file, sep='|', encoding='latin1', on_bad_lines='skip')
        df_cw['GEOID_UA_20'] = pd.to_numeric(df_cw['GEOID_UA_20'], errors='coerce')
        df_final = pd.merge(df_metrics, df_cw, left_on='UACE', right_on='GEOID_UA_20', how='left')
    except Exception as e:
        print(f"Crosswalk merge failed: {e}")
        df_final = df_metrics

    # 4. Save Results
    output_file = "transit_fragmentation_results.csv"
    df_final.to_csv(output_file, index=False)
    print(f"Results saved to {output_file}")
    
    # Print analysis of known fragmented vs consolidated cities
    print("\nSample Fragmentation Analysis:")
    sample_cities = ['New York', 'Chicago', 'Cincinnati', 'Houston', 'Phoenix', 'San Francisco']
    for city in sample_cities:
        match = df_final[df_final['UACE_Name'].str.contains(city, na=False, case=False)]
        if not match.empty:
            top_row = match.sort_values('Total_UPT', ascending=False).iloc[0]
            print(f"{city:15} | Agencies: {int(top_row['Agency_Count']):2} | Fragmentation Index: {top_row['Fragmentation_Index']:.2f} | Total Trips: {top_row['Total_UPT']:,.0f}")

if __name__ == "__main__":
    main()
