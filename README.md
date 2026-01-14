# Capstone Project: Data Pipeline & Analytics

## Overview
This project demonstrates building a full data pipeline from synthetic data generation to visualization and analysis. The goal is to simulate a real-world data workflow including ingestion, cleaning, enrichment, validation, modeling, and visualization.  

The project uses Python for data processing and Power BI / Excel for visualization.

---
  Dataset
- Synthetic dataset generated using [Mockaroo](https://mockaroo.com/)  
- **Rows:** 10,000  
- **Columns:**
  - `CustomerID` – Unique identifier  
  - `Name` – Customer name  
  - `Age` – Customer age  
  - `PurchaseAmount` – Amount spent  
  - `Country` – Country of residence  
  - `Date` – Transaction date  
- Stored as: `data/raw/dataset.csv`  

---

## Project Structure

# Capstone Project: Data Pipeline & Analytics

## Overview
This project demonstrates building a full data pipeline from synthetic data generation to visualization and analysis. The goal is to simulate a real-world data workflow including ingestion, cleaning, enrichment, validation, modeling, and visualization.  

The project uses Python for data processing and Power BI / Excel for visualization.

---

## Dataset
- Synthetic dataset generated using [Mockaroo](https://mockaroo.com/)  
- **Rows:** 10,000  
- **Columns:**
  - `CustomerID` – Unique identifier  
  - `Name` – Customer name  
  - `Age` – Customer age  
  - `PurchaseAmount` – Amount spent  
  - `Country` – Country of residence  
  - `Date` – Transaction date  
- Stored as: `data/raw/dataset.csv`  

---

## Project Structure

capstone-project/
├── data/
│ ├── raw/ # Original dataset
│ └── cleaned/ # Cleaned and enriched dataset
├── dashboards/ # Visualizations
├── logs/ # Validation logs
├── scripts/ # Python scripts for the pipeline
│ ├── clean_transform.py
│ ├── enrich.py
│ ├── validate.py
│ ├── load.py
│ └── pipeline.py
├── diagrams/ # ERD or data modeling diagrams
└── README.md


---

## Pipeline Steps

### 1. Cleaning & Transformation
- Remove duplicates and missing values
- Standardize column names
- Convert `Date` column to datetime format
- Script: `clean_transform.py`

### 2. Enrichment
- Add new features:
  - `age_group` (Teen, Young Adult, Adult, Senior)
  - `purchase_category` (Low, Medium, High, VIP)
- Script: `enrich.py`

### 3. Validation
- Check for missing values and data consistency
- Logs saved in `logs/validation.log`
- Script: `validate.py`

### 4. Loading
- Save cleaned and enriched dataset as:
  - CSV: `data/cleaned/dataset_final.csv`
  - Excel: `data/cleaned/dataset_final.xlsx`
- Script: `load.py`

### 5. Orchestration
- `pipeline.py` automates all steps sequentially
- Usage:
```bash
cd scripts
python pipeline.py
