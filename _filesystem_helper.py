from datetime import datetime
import os

from _init_logging import MyLogger
import _CONSTANTS as CONSTANTS

class FileInfo:
    def __init__(self,
                 file_name: str,
                 full_path: str,
                 size: int,
                 last_modified_at: str) -> None:
        self.file_name = file_name
        self.full_path = full_path
        self.size = size
        self.last_modified_at = last_modified_at

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
        file_full_path = (os.path.join(os.path.curdir, base_path, file_name) if suffix == "" else os.path.join(os.path.curdir, base_path, file_name.split('.')[0] + suffix + "." + file_name.split('.')[-1])).replace("\\", "/")
        return file_full_path

    @staticmethod
    def clean_data_directory() -> None:
        """
        Clean up previously generated encoding example files.
        """
        
        MyLogger.info("\nCleaning encoding example files:START")

        count_files_before_delete = 0
        
        file_names = os.listdir(CONSTANTS.BASE_PATH_DATA_RAW)
        count_files_before_delete += len(file_names)
        for file_name in file_names:
            full_path = FileSystemHelper.calc_file_full_path(CONSTANTS.BASE_PATH_DATA_RAW, file_name)
            if os.path.isfile(full_path):
                MyLogger.debug(f"--> Delete the \"{full_path}\" file.")
                os.remove(full_path)

        file_names = os.listdir(CONSTANTS.BASE_PATH_DATA_PROCESSED)
        count_files_before_delete += len(file_names)
        for file_name in file_names:
            full_path = FileSystemHelper.calc_file_full_path(CONSTANTS.BASE_PATH_DATA_PROCESSED, file_name)
            if os.path.isfile(full_path):
                MyLogger.debug(f"--> Delete the \"{full_path}\" file.")
                os.remove(full_path)
                
        count_files_after_delete = len(os.listdir(CONSTANTS.BASE_PATH_DATA_RAW)) + len(os.listdir(CONSTANTS.BASE_PATH_DATA_PROCESSED))
        MyLogger.debug(f"Files before: {count_files_before_delete}, Files after: {count_files_after_delete}")
        
        MyLogger.info("Cleaning encoding example files:END")

    @staticmethod
    def collect_tree_info(directory: str) -> list[FileInfo]:
        """
        Collects information about all files in the directory and its subdirectories.
        """
        file_info_list = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                full_path = os.path.join(root, file).replace("\\", "/")
                size = os.path.getsize(full_path)
                last_modified_at = datetime.fromtimestamp(os.path.getmtime(full_path)).strftime('%Y-%m-%d %H:%M:%S')
                file_info = FileInfo(
                    file_name=file,
                    full_path=full_path,
                    size=size,
                    last_modified_at=last_modified_at
                )
                file_info_list.append(file_info)
        return file_info_list