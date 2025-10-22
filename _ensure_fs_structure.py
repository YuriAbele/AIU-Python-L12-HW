# This script ensures the specified filesystem structure exists.

import os

import _CONSTANTS as CONSTANTS
from _init_logging import MyLogger


def ensure_fs_structure():
    """
    Ensure the filesystem structure defined in FS_TEMPLATE exists.
    """
    MyLogger.info(f"\nEnsuring filesystem structure:START\n{CONSTANTS.FS_STRUCTURE}\n")
    for path in CONSTANTS.FS_STRUCTURE:
        MyLogger.debug(f"--> Ensuring directory exists: {path}")
        os.makedirs(path, exist_ok=True)
    MyLogger.info("Ensuring filesystem structure:END")