from datetime import datetime
import os
import hashlib

from . import CONSTANTS as CONSTANTS
from .logging_helper import LoggingHelper
from .file_info import FileInfo

class FileSystemHelper:
    
    @staticmethod
    def ensure_fs_structure():
        """
        Ensure the filesystem structure defined in FS_TEMPLATE exists.
        """
        LoggingHelper.info(f"\nEnsuring filesystem structure:START\n{CONSTANTS.FS_STRUCTURE}\n")
        for path in CONSTANTS.FS_STRUCTURE:
            LoggingHelper.debug(f"--> Ensuring directory exists: {path}")
            os.makedirs(path, exist_ok=True)
        LoggingHelper.info("Ensuring filesystem structure:END")

#######################################################################################################
    
    @staticmethod
    def calc_file_full_path(base_path: str, file_name: str, suffix: str = "") -> str:
        """
        Calculate the full file path by joining the base path and file name.
        """
        file_full_path = (os.path.join(os.path.curdir, base_path, file_name) if suffix == "" else os.path.join(os.path.curdir, base_path, file_name.split('.')[0] + suffix + "." + file_name.split('.')[-1])).replace("\\", "/")
        return file_full_path

#######################################################################################################

    @staticmethod
    def clean_data_directory() -> None:
        """
        Clean up previously generated encoding example files.
        """
        
        LoggingHelper.info("\nCleaning encoding example files:START")

        count_files_before_delete = 0
        
        file_names = os.listdir(CONSTANTS.BASE_PATH_DATA_RAW)
        count_files_before_delete += len(file_names)
        for file_name in file_names:
            full_path = FileSystemHelper.calc_file_full_path(CONSTANTS.BASE_PATH_DATA_RAW, file_name)
            if os.path.isfile(full_path):
                LoggingHelper.debug(f"--> Delete the \"{full_path}\" file.")
                os.remove(full_path)

        file_names = os.listdir(CONSTANTS.BASE_PATH_DATA_PROCESSED)
        count_files_before_delete += len(file_names)
        for file_name in file_names:
            full_path = FileSystemHelper.calc_file_full_path(CONSTANTS.BASE_PATH_DATA_PROCESSED, file_name)
            if os.path.isfile(full_path):
                LoggingHelper.debug(f"--> Delete the \"{full_path}\" file.")
                os.remove(full_path)
                
        count_files_after_delete = len(os.listdir(CONSTANTS.BASE_PATH_DATA_RAW)) + len(os.listdir(CONSTANTS.BASE_PATH_DATA_PROCESSED))
        LoggingHelper.debug(f"Files before: {count_files_before_delete}, Files after: {count_files_after_delete}")
        
        LoggingHelper.info("Cleaning encoding example files:END")

#######################################################################################################

    @staticmethod
    def collect_tree_info(directory_path: str) -> list[FileInfo]:
        """
        Collects information about all files in the directory and its subdirectories.
        """
        
        LoggingHelper.info(f"\nCollecting tree info for directory:START\n{directory_path}")
        
        file_info_list = []
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                full_path = os.path.join(root, file).replace("\\", "/")
                size = os.path.getsize(full_path)
                last_modified_at = datetime.fromtimestamp(os.path.getmtime(full_path)).strftime('%Y-%m-%d %H:%M:%S')
                hash = FileSystemHelper.calculate_file_hash(full_path)
                file_info = FileInfo(
                    file_name=file,
                    full_path=full_path,
                    size=size,
                    last_modified_at=last_modified_at,
                    hash=hash
                )
                file_info_list.append(file_info)
                
                
        LoggingHelper.info(f"Collecting tree info for directory:END")
        return file_info_list

#######################################################################################################

    @staticmethod
    def calculate_file_hash(file_path: str, hash_algorithm: str = "sha256", block_size: int = 65536) -> str | None:
        """
        Calculates the hash of a file by reading it in chunks.

        :param filename: Path to the file
        :param hash_algorithm: Hashing algorithm (e.g., 'sha256', 'md5', 'sha1')
        :param block_size: Size of the block to read the file (in bytes)
        :return: A string with the hash in hexadecimal format, or None on error
        """
        
        LoggingHelper.info(f"\nCalculating file hash:START")
        LoggingHelper.debug(f"--> File: {file_path}\n--> Algorithm: {hash_algorithm}\n--> Block size: {block_size} bytes")
        
        # Create a hash object
        try:
            hash_obj = hashlib.new(hash_algorithm)
        except ValueError:
            LoggingHelper.error(f"Error: Unsupported hash algorithm '{hash_algorithm}'")
            return None

        result = None
        try:
            # Open the file for reading in binary mode ('rb')
            with open(file_path, 'rb') as f:
                # Read the file in blocks until the end is reached
                # iter(lambda: f.read(block_size), b'') is an efficient way to loop
                for block in iter(lambda: f.read(block_size), b''):
                    # Update the hash object with each block of data
                    hash_obj.update(block)
            
            # Return the hash as a hexadecimal string
            result = hash_obj.hexdigest()

        except FileNotFoundError:
            LoggingHelper.error(f"Error: File not found '{file_path}'")
            result = None
        except IOError as e:
            LoggingHelper.error(f"Error reading file '{file_path}': {e}")
            result = None
            
        LoggingHelper.info(f"Calculating file hash:END\nHash: {result}")
        return result
    
#######################################################################################################
