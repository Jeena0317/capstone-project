import os
import subprocess
import logging
import sys

# -------------------- Configuration --------------------
BASE_DIR = r"C:\Users\alley\OneDrive\Desktop\Capstone_Project"
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")
LOGS_DIR = os.path.join(BASE_DIR, "logs")

os.makedirs(LOGS_DIR, exist_ok=True)

# -------------------- Logging Setup --------------------
logging.basicConfig(
    filename=os.path.join(LOGS_DIR, "pipeline.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -------------------- Helper Function --------------------
def run_step(script_name):
    script_path = os.path.join(SCRIPTS_DIR, script_name)
    logging.info(f"Starting {script_name}")

    result = subprocess.run(
        [sys.executable, script_path],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        logging.error(f"Error in {script_name}")
        logging.error(result.stderr)
        raise Exception(f"{script_name} failed")

    logging.info(f"Completed {script_name}")

# -------------------- Pipeline Execution --------------------
try:
    logging.info("Pipeline started")

    run_step("clean_transform.py")
    run_step("enrich.py")
    run_step("validate.py")
    run_step("load.py")

    logging.info("Pipeline completed successfully")

except Exception as e:
    logging.error("Pipeline failed", exc_info=True)
    sys.exit(1)
