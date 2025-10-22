from datetime import datetime

from ensure_fs_structure import ensure_fs_structure
from init_logging import MyLogger

################################################################################

MyLogger.log_start()

ensure_fs_structure()

MyLogger.info("This is an info message.")
MyLogger.debug("This is a debug message.")
MyLogger.error("This is an error message.")

MyLogger.log_end()

################################################################################
