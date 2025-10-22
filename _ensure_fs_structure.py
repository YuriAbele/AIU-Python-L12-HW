# This script ensures the specified filesystem structure exists.

import os

from _init_logging import MyLogger

FS_TEMPLATE = [
    "project_root",
    "project_root/data",
    "project_root/data/raw",
    "project_root/data/processed",
    "project_root/logs",
    "project_root/backups",
    "project_root/output",
]

def ensure_fs_structure():
    """
    Ensure the filesystem structure defined in FS_TEMPLATE exists.
    """
    MyLogger.info(f"Ensuring filesystem structure...\n{FS_TEMPLATE}")
    for path in FS_TEMPLATE:
        MyLogger.debug(f"--> Ensuring directory exists: {path}")
        os.makedirs(path, exist_ok=True)
    MyLogger.info("Filesystem structure ensured.")