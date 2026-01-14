# validate.py
import pandas as pd
import logging
import os

print("Step 3: Validating data...")

# Set up logging
log_path = os.path.join("..", "logs", "validation.log")
logging.basicConfig(filename=log_path, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Load enriched data
enriched_path = os.path.join("..", "data", "cleaned", "dataset_enriched.csv")
df = pd.read_csv(enriched_path)

# Check for missing values
if df.isnull().sum().sum() == 0:
    logging.info("No missing values found")
else:
    missing = df.isnull().sum()
    logging.warning(f"Missing values detected:\n{missing}")

# Check for duplicates
duplicates = df.duplicated().sum()
if duplicates == 0:
    logging.info("No duplicate rows found")
else:
    logging.warning(f"Duplicate rows detected: {duplicates}")

print(f"Validation complete! Logs saved to {log_path}")
