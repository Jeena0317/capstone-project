import pandas as pd
import os

print("Step 1: Cleaning and transforming data...")

# Path to raw data
raw_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw', 'dataset.csv')
df = pd.read_csv(raw_path)

# Drop duplicates and missing values
df = df.drop_duplicates().dropna()

# Clean column names
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Correctly parse dates
df['date'] = pd.to_datetime(df['date'], dayfirst=True)

# Save cleaned data
cleaned_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'cleaned', 'dataset_cleaned.csv')
df.to_csv(cleaned_path, index=False)

print("Cleaning complete!")
