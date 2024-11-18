import os
import logging
from pathlib import Path

log_dir = Path(os.getenv("APPDATA",".")) / "LearnReflect"
log_dir.mkdir(parents=True,exist_ok=True)



log_file = log_dir / "LearnReflect.txt"
logging.basicConfig(
    filename=str(log_file),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)