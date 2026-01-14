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
│
├── data/
│ ├── raw/
│ │ └── dataset.csv # Original dataset from Mockaroo
│ └── cleaned/
│ ├── dataset_cleaned.csv
│ ├── dataset_enriched.csv
│ └── dataset_final.csv
│
├── scripts/
│ ├── clean_transform.py # Data cleaning & transformation
│ ├── enrich.py # Feature enrichment
│ ├── validate.py # Data validation
│ ├── load.py # Load final dataset
│ └── pipeline.py # Orchestration script
│
├── dashboards/
│ └── dashboard.pbix # Power BI / Excel visuals
│
├── logs/
│ └── validation.log # Pipeline logs
│
│
└── README.md


---

### **Step 3: Save the file**
- Press **Ctrl + S**

---

### **Step 4: Check on GitHub**
- Commit and push again:
```bash
git add README.md
git commit -m "Fix project structure formatting"
git push


Refresh your GitHub repo →
✅ The structure will now look clean, readable, and professional

💡 Why this works

Triple backticks ``` keep formatting

Tree layout matches real project structure

This is industry-standard README style

Evaluators love this clarity

If you want, I can also:

✔️ Fix the entire README end-to-end

✔️ Make it submission-ready

✔️ Match Data Engineer / Data Analyst standards

Just tell me 👍

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
