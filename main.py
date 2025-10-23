from pathlib import Path
from pprint import pprint

from helpers import *

LoggingHelper.log_start()
################################################################################

# Task 1.1. Ensure the file system structure is in place
FileSystemHelper.ensure_fs_structure()

################################################################################
LoggingHelper.print_split_line()

# Task 1.2. Generate encoding example files
FileSystemHelper.clean_data_directory()
EncodingExamples.encoding_examples_generate()

################################################################################
LoggingHelper.print_split_line()

# Task 2.1. Read and process encoding example files
EncodingExamples.encoding_examples_read_and_process()

################################################################################
LoggingHelper.print_split_line()

# Task 2.2. Read multiple processed files and serialize to JSON
many_files_list = SerializationHelper.read_many_files()
json_string = SerializationHelper.serialize_list_to_json_array(many_files_list)
output_path = FileSystemHelper.calc_file_full_path(CONSTANTS.BASE_PATH_OUTPUT, CONSTANTS.FILE_NAME_JSON_OUTPUT_FILE_PAIRS)
SerializationHelper.save_json_to_file(json_string, output_path)

################################################################################
LoggingHelper.print_split_line()

# Task 3.1. Backup data
file_infos_before_backup = FileSystemHelper.collect_tree_info(CONSTANTS.BASE_PATH_DATA)
BackupHelper.backup_data(CONSTANTS.BASE_PATH_DATA)

################################################################################
LoggingHelper.print_split_line()

# Task 3.2. Restore data
FileSystemHelper.clean_data_directory()
full_path_latest_backup = BackupHelper.get_last_backup_full_path()
BackupHelper.restore_data(full_path_latest_backup, CONSTANTS.BASE_PATH_DATA)
file_infos_after_restore = FileSystemHelper.collect_tree_info(CONSTANTS.BASE_PATH_DATA)
are_file_infos_before_and_after_restore_equal = SerializationHelper.compare_fileinfo_lists(file_infos_before_backup, file_infos_after_restore)
LoggingHelper.info(f"Are the original and restored file info lists equal? - {are_file_infos_before_and_after_restore_equal}")

################################################################################
LoggingHelper.print_split_line()

file_infos_to_serialize = FileSystemHelper.collect_tree_info(CONSTANTS.BASE_PATH_DATA_PROCESSED)
print(*file_infos_to_serialize, sep="\n")
json_string = SerializationHelper.serialize_list_to_json_array(file_infos_to_serialize)
output_path = FileSystemHelper.calc_file_full_path(CONSTANTS.BASE_PATH_OUTPUT, CONSTANTS.FILE_NAME_JSON_OUTPUT_FILE_INFOS)
SerializationHelper.save_json_to_file(json_string, output_path)
LoggingHelper.debug_file_contents(output_path, message="Contents of the file infos JSON output file:")
file_infos_deserialized = SerializationHelper.deserialize_json_array_to_fileinfo_list(json_string)
are_original_and_deserialized_lists_equal = SerializationHelper.compare_fileinfo_lists(file_infos_to_serialize, file_infos_deserialized)
LoggingHelper.info(f"Are the original and deserialized file info lists equal? - {are_original_and_deserialized_lists_equal}")

print(FileSystemHelper.calculate_file_hash(output_path))

################################################################################
LoggingHelper.log_end()
