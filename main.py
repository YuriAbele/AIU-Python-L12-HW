from pathlib import Path

from _backup_helper import BackupHelper
from _init_logging import MyLogger
from _filesystem_helper import FileSystemHelper
from _encoding_examples import EncodingExamples
from _serialization_helper import SerializationHelper
import _CONSTANTS as CONSTANTS

MyLogger.log_start()
################################################################################

# Task 1.1. Ensure the file system structure is in place
FileSystemHelper.ensure_fs_structure()

################################################################################
MyLogger.print_split_line()

# Task 1.2. Generate encoding example files
FileSystemHelper.clean_data_directory()
EncodingExamples.encoding_examples_generate()

################################################################################
MyLogger.print_split_line()

# Task 2.1. Read and process encoding example files
EncodingExamples.encoding_examples_read_and_process()

################################################################################
MyLogger.print_split_line()

# Task 2.2. Read multiple processed files and serialize to JSON
many_files_list = SerializationHelper.read_many_files()
json_string = SerializationHelper.serialize_files_pair_data_to_json(many_files_list)
SerializationHelper.save_json_to_file(json_string)

################################################################################
MyLogger.print_split_line()

# Task 3.1. Backup data
BackupHelper.backup_data(CONSTANTS.BASE_PATH_DATA)

################################################################################
MyLogger.print_split_line()

# Task 3.2. Restore data
FileSystemHelper.clean_data_directory()
full_path_latest_backup = BackupHelper.get_last_backup_full_path()
BackupHelper.restore_data(full_path_latest_backup, CONSTANTS.BASE_PATH_DATA)

################################################################################
MyLogger.log_end()
