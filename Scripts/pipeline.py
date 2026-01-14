# pipeline.py
import subprocess
import os

print("Starting pipeline...")

# Set the working directory to the folder where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Scripts to run (ensure these files exist in the same folder)
scripts = [
    'clean_transform.py',
    'enrich.py',
    'validate.py',
    'load.py'
]

for script in scripts:
    script_path = os.path.join(script_dir, script)
    if os.path.exists(script_path):
        print(f"Running {script}...")
        subprocess.run(['python', script_path], check=True)
    else:
        print(f"Warning: {script} not found at {script_path}")

print("Pipeline completed successfully!")
