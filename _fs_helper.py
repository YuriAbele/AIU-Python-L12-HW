import os

from _init_logging import MyLogger
import _CONSTANTS as CONSTANTS

class FileSystemHelper:
    
    @staticmethod
    def ensure_fs_structure():
        """
        Ensure the filesystem structure defined in FS_TEMPLATE exists.
        """
        MyLogger.info(f"\nEnsuring filesystem structure:START\n{CONSTANTS.FS_STRUCTURE}\n")
        for path in CONSTANTS.FS_STRUCTURE:
            MyLogger.debug(f"--> Ensuring directory exists: {path}")
            os.makedirs(path, exist_ok=True)
        MyLogger.info("Ensuring filesystem structure:END")
    
    
    @staticmethod
    def calc_file_full_path(base_path: str, file_name: str, suffix: str = "") -> str:
        """
        Calculate the full file path by joining the base path and file name.
        """
        file_full_path = (os.path.join(base_path, file_name) if suffix == "" else os.path.join(base_path, file_name.split('.')[0] + suffix + "." + file_name.split('.')[-1])).replace("\\", "/")
        return file_full_path
