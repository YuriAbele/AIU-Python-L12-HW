from _init_logging import MyLogger
from _ensure_fs_structure import ensure_fs_structure
from _encoding_examples import EncodingExamples
from _serialize_processor import SerializeProcessor

################################################################################

MyLogger.log_start()

# Task 1.1. Ensure the file system structure is in place
ensure_fs_structure()

# Task 1.2. Generate encoding example files
EncodingExamples.clean_target_files()
EncodingExamples.encoding_examples_generate()

# Task 2.1. Read and process encoding example files
EncodingExamples.encoding_examples_read_and_process()

# Task 2.2. Read multiple processed files and serialize to JSON
many_files_list = SerializeProcessor.read_many_files()
json_string = SerializeProcessor.serialize_to_json(many_files_list)
SerializeProcessor.save_json_to_file(json_string)

MyLogger.log_end()

################################################################################
