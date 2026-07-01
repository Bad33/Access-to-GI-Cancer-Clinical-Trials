# Geographical Equity in Access to GI Cancer Clinical Trials

This repository contains the analysis scripts and notebooks used for the GI Cancer Clinical Trials research. 

## Research Overview
- **Objective:** Evaluate geographical equity in access to GI cancer clinical trials.
- **Methods:** Python, Pandas, NumPy, Geospatial Modeling. Engineered a data pipeline to extract, clean, and process 958 clinical trials from ClinicalTrials.gov, geocoding trial sites across 4,400+ US ZIP codes and integrating multi-source datasets (Census ZCTAs, RUCA rurality codes, ACS income and race/ethnicity data).
- **Findings:** Applied Haversine distance-based proximity modeling to compute population access within 30 and 60-mile radii, revealing rural HCC patients had only 9.6% trial access vs 71% urban.

## Project Structure
- `GI-Cancer_Script-V1.ipynb`: Primary exploration notebook.
- `script/`: Contains the core data extraction and analysis notebooks (`Extract_Zipcodes.ipynb`, `get-all-data-augmented.ipynb`, `revised_gi_trials_coverage.ipynb`).
- `zip_zcta_crosswalk.py`: Utility script for ZIP to ZCTA crosswalking.
- `out/`: Contains selected results and figures from the analysis.

## Expected Data Structure
The raw data is not included in this repository due to size and privacy constraints. To run the scripts, the following data structure is expected in the root directory:

```
data/
├── RUCA-codes-2020-zipcode.csv
├── acs/
│   ├── acs5y_2023_zcta_b01003.csv
│   ├── acs5y_2023_zcta_b03002.csv
│   └── acs5y_2023_zcta_b19013.csv
├── cancer/
│   ├── Oesophageal_cancer.csv
│   ├── cholangiocarcinoma.csv
│   ├── colorectal_cancer.csv
│   ├── gastric_cancer.csv
│   ├── hepatocellular_cancer.csv
│   └── pancreatic_cancer.csv
├── tl_2020_us_state/
│   └── tl_2020_us_state.shp
└── tl_2020_us_zcta510/
    └── tl_2020_us_zcta510.shp
```
