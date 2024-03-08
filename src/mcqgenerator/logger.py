import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
print('This is the LOG_FILE :', LOG_FILE)

log_path = os.path.join(os.getcwd(), "logs")
print('This is the log_path :', log_path)

os.makedirs(log_path, exist_ok = True)

LOG_FILEPATH = os.path.join(log_path, LOG_FILE)
print('This is the LOG_FILEPATH :', LOG_FILEPATH)

logging.basicConfig( level = logging.INFO,
        filename = LOG_FILEPATH,
        format = "%[(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
        )
