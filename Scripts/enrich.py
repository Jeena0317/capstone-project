# enrich.py
import pandas as pd
import os

print("Step 2: Enriching data...")

# Paths
cleaned_path = os.path.join("..", "data", "cleaned", "dataset_cleaned.csv")
enriched_path = os.path.join("..", "data", "cleaned", "dataset_enriched.csv")

# Load cleaned data
df = pd.read_csv(cleaned_path)

# Create age groups
df['age_group'] = pd.cut(df['age'], bins=[0, 18, 35, 50, 100],
                         labels=['Teen', 'Young Adult', 'Adult', 'Senior'])

# Create purchase categories
df['purchase_category'] = pd.cut(df['purchaseamount'],
                                 bins=[0, 100, 500, 1000, 5000],
                                 labels=['Low', 'Medium', 'High', 'VIP'])

# Save enriched data
df.to_csv(enriched_path, index=False)

print(f"Enrichment complete! Saved to {enriched_path}")
