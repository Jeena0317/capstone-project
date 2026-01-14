# load.py
import pandas as pd
import os

print("Step 4: Loading final data...")

# Paths
enriched_path = os.path.join("..", "data", "cleaned", "dataset_enriched.csv")
final_csv_path = os.path.join("..", "data", "cleaned", "dataset_final.csv")
final_excel_path = os.path.join("..", "data", "cleaned", "dataset_final.xlsx")

# Load enriched data
df = pd.read_csv(enriched_path)

# Save final CSV
df.to_csv(final_csv_path, index=False)
# Save Excel version
df.to_excel(final_excel_path, index=False)

print(f"Data loading complete! Saved to:\n{final_csv_path}\n{final_excel_path}")
