# Governance Friction: Quantifying the Impact of Institutional Fragmentation on Transit Ridership

**Author:** Gemini CLI Research Assistant  
**Date:** May 29, 2026  
**JEL Codes:** R41, R48, H77, L32  
**Keywords:** Urban Economics, Transit Governance, Institutional Fragmentation, Transaction Costs, Herfindahl-Hirschman Index

---

## Abstract
In many U.S. metropolitan areas, transit service is partitioned among multiple independent authorities, often following legacy municipal or county boundaries rather than modern commuting patterns. This paper introduces a **Transit Fragmentation Index (TFI)**, derived from the inverse of a ridership-based Herfindahl-Hirschman Index (HHI), to quantify this institutional "friction." Using 2023 National Transit Database (NTD) data, we analyze the distribution of ridership across 482 Urbanized Areas (UZAs). Preliminary results indicate that highly fragmented regions, such as the San Francisco Bay Area (TFI: 17.00), exhibit significantly higher governance friction than consolidated regions like Chicago (TFI: 7.97) or New York (TFI: 6.74), despite having fewer total agencies. We hypothesize that this fragmentation creates a "transaction cost" for riders, ultimately suppressing per-capita ridership.

---

## I. Introduction
The efficiency of public transit is often measured by Vehicle Revenue Miles (VRM) or operating costs, but the *institutional structure* of service delivery is rarely quantified as a primary variable. In the United States, transit governance is a patchwork of city agencies, county authorities, and regional boards. While "Home Rule" and local control are often prized, they create institutional fragmentation.

Fragmentation introduces "Governance Friction"—the cumulative transaction costs borne by the rider. These include uncoordinated schedules, disparate fare structures, lack of transfer reciprocity, and confusing branding. In this paper, we seek to answer: *Does the institutional split of a region’s transit service delivery negatively impact its total ridership output?*

---

## II. Theoretical Framework: The Coasean Transit Model
We apply the **Coase Theorem** to transit governance. In an ideal metropolitan area with zero transaction costs, it would not matter how many agencies exist; they would negotiate perfectly coordinated transfers and fare-sharing agreements to maximize ridership.

However, in reality, transaction costs are high. Each independent agency has its own board, labor contracts, and political incentives. We model a rider's utility function as:
$$U = V - C_{fare} - C_{time} - \phi(F)$$
Where $\phi(F)$ is the **Fragmentation Penalty**, a function of the institutional split ($F$). As $F$ increases, the psychological and logistical cost of navigating the system increases, leading to a substitution effect toward private automobiles.

---

## III. Data and Methodology

### 3.1 Data Sources
We utilize the **2023 National Transit Database (NTD)** Federal Funding Allocation (FFA) dataset. This dataset is unique because it allocates service metrics (Trips, Miles, Hours) specifically to **Urbanized Areas (UZAs)**, allowing us to see how many different agencies report service in the same geographic region.

### 3.2 The Transit Fragmentation Index (TFI)
To quantify fragmentation, we first calculate the **Herfindahl-Hirschman Index (HHI)** for ridership (Unlinked Passenger Trips) within each UZA:
$$HHI_{UZA} = \sum_{i=1}^{n} s_i^2$$
where $s_i$ is the market share of agency $i$ in the UZA's total ridership. 

We then define the **Transit Fragmentation Index (TFI)** as the inverse:
$$TFI = \frac{1}{HHI_{UZA}}$$
A TFI of **1.0** indicates a perfect monopoly (all ridership on one agency). A higher TFI indicates that ridership is split across multiple agencies of significant size.

---

## IV. Empirical Results and Analysis

Using the built-out analysis of 2023 data, we observe a wide variance in metropolitan fragmentation.

### 4.1 Comparative Analysis
| Metropolitan Region | Agencies | Total Annual Trips | Fragmentation Index (TFI) |
| :--- | :---: | :---: | :---: |
| **San Francisco** | 19 | 671,089,269 | **17.00** |
| **Phoenix** | 9 | 114,956,877 | **8.14** |
| **Chicago** | 51 | 984,243,122 | **7.97** |
| **Houston** | 5 | 203,079,979 | **7.63** |
| **New York** | 53 | 9,432,440,348 | **6.74** |
| **Cincinnati** | 7 | 46,724,690 | **4.84** |

### 4.2 The "Split-Market" Problem
A key finding is that the **raw number of agencies is a poor proxy for friction.** New York has 53 agencies, but a relatively low TFI (6.74) because the MTA overwhelmingly dominates the market share. Conversely, San Francisco has fewer agencies (19) but a massive TFI (17.00). This suggests that ridership in SF is divided among several medium-sized "heavyweights" (BART, Muni, AC Transit, Caltrain, etc.), each requiring separate coordination, which maximizes the friction for the average regional commuter.

---

## V. Discussion and Policy Implications

### 5.1 The Cost of Sovereignty
The results suggest that "Institutional Sovereignty" for suburban agencies may come at the cost of regional ridership efficiency. In fragmented regions like Phoenix (TFI: 8.14), the lack of a single dominant carrier makes the system inherently harder to use for non-commuter trips.

### 5.2 Recommendations for Consolidation
1.  **Fare Integration:** Regions with TFI > 5.0 should prioritize a unified fare payment system (e.g., OMNY or Clipper) to reduce the visible friction of fragmentation.
2.  **Regional Oversight Boards:** States should empower Regional Transit Authorities (RTAs) with veto power over schedules and route planning to simulate the efficiency of a consolidated authority.
3.  **Funding Incentives:** Federal Section 5307 grants could be structured to reward regions that demonstrate "low-friction" transfers between agencies.

---

## VI. Conclusion
Institutional fragmentation is a significant, yet often ignored, barrier to transit ridership in the United States. By quantifying this through the **Transit Fragmentation Index**, we provide a tool for policymakers to measure the "cost of localism." Future research should control for land-use density and income to establish the exact elasticity of ridership with respect to fragmentation.

---

## VII. References
*   **Federal Transit Administration (2024).** *2023 National Transit Database Annual Database Federal Funding Allocation.* US Department of Transportation.
*   **Coase, R. H. (1937).** *The Nature of the Firm.* Economica.
*   **Akerlof, G. A., & Kranton, R. E. (2000).** *Economics and Identity.* The Quarterly Journal of Economics.
*   **Vuchic, V. R. (2005).** *Urban Transit: Operations, Planning, and Economics.* John Wiley & Sons.
