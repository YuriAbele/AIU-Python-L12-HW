# This script ensures the specified filesystem structure exists.

import os

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
    for path in FS_TEMPLATE:
        os.makedirs(path, exist_ok=True)
    print("Ensure the Filesystem structure exists!")
