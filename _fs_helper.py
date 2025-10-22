import os

class FileSystemHelper:
    
    @staticmethod
    def ensure_fs_structure():
        """
        Ensure that the filesystem structure defined in FS_TEMPLATE exists.
        Create directories if they do not exist.
        """
    
    @staticmethod
    def calc_file_full_path(base_path: str, file_name: str, suffix: str = "") -> str:
        """
        Calculate the full file path by joining the base path and file name.
        """
        file_full_path = os.path.join(base_path, file_name) if suffix == "" else os.path.join(base_path, file_name.split('.')[0] + suffix + "." + file_name.split('.')[-1])
        return file_full_path
