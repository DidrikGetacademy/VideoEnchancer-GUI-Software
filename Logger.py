import os
import sys
import logging
from pathlib import Path
log_dir = Path(os.getenv("APPDATA",".")) / "LearnReflect"
log_dir.mkdir(parents=True,exist_ok=True)



log_file = log_dir / "LearnReflect.txt"
logging.basicConfig(
    filename=str(log_file),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - [%(funcName)s:%(lineno)d] - %(message)s",
)
logger = logging.getLogger(__name__)



#Function too debug paths in bundled enviorment.
def debug_bundled_environment():
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
        print(f"Extracted base path: {base_path}")
        print("Contents of base path:")
        for root, dirs, files in os.walk(base_path):
            print(f"\nRoot: {root}")
            print(f"Directories: {dirs}")
            print(f"Files: {files}")
    else:
        print("Not running in bundled mode.")
        
#debug_bundled_environment()

