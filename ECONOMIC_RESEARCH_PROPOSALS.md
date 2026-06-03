# Economic Research Proposals: Urban Dynamics, Public Finance, and Social Persistence

This document outlines four "fully fleshed out" and publishable economic research projects derived from the initial research ideas. Each project includes a theoretical framework, identification strategy, and specific data sources.

---

## 1. The Opportunity Cost of Public Safety: Evaluating the Long-run Impact of Education vs. Police Levies
**JEL Codes:** H72, K42, I22, R51

### **Abstract**
Does a dollar invested in education prevent more crime than a dollar invested in policing? This paper exploits a boundary-discontinuity and close-election regression design (RD) in the state of Ohio, where local tax levies for schools and safety forces (police/fire) are voted on frequently. We compare municipalities that narrowly passed a "new money" education levy versus those that narrowly passed a police levy to estimate the relative efficacy of these expenditures on crime rates, property values, and family stability over a 5-10 year horizon.

### **Theoretical Framework**
We model the municipal budget as a choice between **Direct Deterrence** (policing) and **Human Capital Investment** (education). While policing offers an immediate increase in the probability of detection ($p$), education increases the future opportunity cost of crime by raising wages ($w$). We test the hypothesis that for neighborhoods below a certain SES threshold, the marginal return on education (in terms of crime reduction) exceeds that of policing.

### **Data & Methodology**
*   **Identification Strategy:** Regression Discontinuity (RD). We focus on "close elections" (vote share 49-51%) to isolate exogenous shocks to funding.
*   **Data Sources:**
    *   **Ohio Secretary of State:** Historical Local Tax Levy results (Excel spreadsheets available back to 2013).
    *   **FBI UCR/NIBRS:** Crime statistics at the municipal and county level.
    *   **ACS 5-Year Estimates:** Family formation (marriage rates, children per household) and SES factors.
    *   **County Auditor Data:** Property value appreciation as a proxy for neighborhood "quality of life."

### **Policy Implication**
In an era of "levy fatigue," this research helps city councils and school boards prioritize requests that provide the highest "social ROI" to the community.

---

## 2. Breaking the Blight: Blight Remediation as a Catalyst for Public Safety and Political Economy
**JEL Codes:** R38, H76, K42, D72

### **Abstract**
This project evaluates the impact of Ohio’s **$500 Million BUILDS initiative** (2021–2025) on local crime rates and the political feasibility of safety levies. We test two hypotheses: (1) Blight remediation (demolition and revitalization) serves as a "Broken Windows" deterrent that reduces crime significantly. (2) Visible physical improvements reduce the "perceived need" for police expansion, potentially making voters less likely to approve new police levies (a substitution effect in political economy).

### **Theoretical Framework**
We utilize a **Spatial Competition Model** where blighted properties exert a negative externality on surrounding "law-abiding" capital. Remediation removes the "coordination failure" of vacant lots that harbor criminal activity. Politically, we model the voter's utility function as a trade-off between "Security via Force" (Police) and "Security via Environment" (Remediation).

### **Data & Methodology**
*   **Identification Strategy:** Difference-in-Differences (DiD) with staggered adoption, using the timing of Ohio Department of Development grant awards (Aug 2024, Nov 2024, Dec 2024) as exogenous shocks.
*   **Data Sources:**
    *   **Ohio Department of Development:** Building Demolition and Site Revitalization Program awards ($310M+ to 6,200 projects).
    *   **Local GIS Data:** Specific addresses of demolished blighted structures (from County Land Banks).
    *   **Ohio SOS:** Voter results on subsequent police levies in the same jurisdictions.

### **Policy Implication**
If remediation reduces crime at a lower cost than permanent police payroll, "Land Bank" funding may be the most efficient public safety tool available to urban mayors.

---

## 3. Governance Friction: Institutional Fragmentation and Transit Ridership Efficiency
**JEL Codes:** R41, R48, H77, L32

### **Abstract**
In many U.S. metropolitan areas, transit service is split across multiple independent authorities (e.g., Cincinnati's SORTA, TANK, and BCRTA). This paper quantifies the "fragmentation tax" on transit ridership. Using a Cross-MSA analysis, we calculate a **Transit Fragmentation Index (TFI)** and test whether higher fragmentation correlates with lower per-capita ridership, holding density and income constant.

### **Theoretical Framework**
We apply the **Coase Theorem** to transit governance. Transaction costs (uncoordinated schedules, separate fare cards, lack of route transfers) create "governance friction" for riders. We hypothesize that for a given level of total service (Vehicle Revenue Miles), a unified authority produces higher ridership (Unlinked Passenger Trips) than a fragmented one.

### **Data & Methodology**
*   **Identification Strategy:** Instrumental Variables (IV). We use "Historical Number of Municipalities in 1950" as an instrument for modern transit fragmentation to address endogeneity.
*   **Data Sources:**
    *   **National Transit Database (NTD):** Federal Funding Allocation (FFA) tables to count agencies and UPT per Urbanized Area (UACE).
    *   **BTS Intermodal Passenger Connectivity Database:** To measure the quality of "transfers" between agencies.
    *   **Census TIGER/Line:** For spatial density controls.

### **Policy Implication**
Provides empirical support for regional transit consolidation or "RTA-style" oversight boards to reduce friction and increase ROI on transit spending.

---

## 4. The "Sticker" Effect: Social Persistence and the Transmission of Neighborhood Norms
**JEL Codes:** R23, Z13, D91, J13

### **Abstract**
Does being surrounded by "stickers" (long-term residents) influence a mobile person to stay? This research investigates the social spillovers of residential stability. Using the **Akerlof-Kranton framing of Identity Economics**, we test whether the presence of a "stable core" in a neighborhood alters the identity of newcomers from "transient" to "local," thereby increasing their persistence and potentially their fertility rates.

### **Theoretical Framework**
We model "Neighborhood Identity" as a social norm. Moving costs are not just pecuniary but identity-based. Living near people who have stayed for 20+ years creates a "Sticker Norm" that increases the psychological cost of moving out, effectively acting as a social anchor.

### **Data & Methodology**
*   **Identification Strategy:** Network/Spillover Regression. We look at newcomers (residents <2 years) and their probability of staying for 5+ years based on the proportion of 20+ year residents in their Census Tract.
*   **Data Sources:**
    *   **ACS Public Use Microdata Sample (PUMS):** "Length of Tenure" and "Mobility in last year" variables.
    *   **IRS Statistics of Income (SOI):** Migration data at the county-to-county level.
    *   **Census "Time in Neighborhood" Tables:** Tract-level counts of residents by years in home.

### **Policy Implication**
Highlights the importance of "aging in place" policies not just for seniors, but as a mechanism for stabilizing the entire neighborhood's social fabric and family formation.

---

## Next Steps for Data Acquisition

1.  **Ohio SOS Data:** Download the "Local Tax Levy" Excel files. I recommend a Python script using `pandas` to filter `ISSUE_TYPE == 'POLICE'` and `ISSUE_TYPE == 'SCHOOL'`.
2.  **NTD Data:** The `2023_FFA_Database.xlsx` is the primary file for the Transit Fragmentation project. Group by `UACE_CD` and count unique `NTD_ID`s.
3.  **Blight Data:** The Ohio Department of Development releases lists of funded projects. These should be merged with local crime heatmaps from Open Data portals (e.g., Cincinnati's CincyInsights).
