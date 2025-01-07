import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"logging.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),  ##This logs into the logging.log file
        logging.StreamHandler(sys.stdout)   ##This instantly shows logs on the cmd while we run the file.
    ]
)
logger = logging.getLogger("DataScience_proj1_Logger")