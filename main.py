from _init_logging import MyLogger
from _ensure_fs_structure import ensure_fs_structure
from _encoding_examples import EncodingExamples

################################################################################

MyLogger.log_start()

# Task 1.1. Ensure the file system structure is in place
ensure_fs_structure()

# Task 1.2. Generate encoding example files
EncodingExamples.clean_target_files()
EncodingExamples.encoding_examples_generate()

# Task 2.1. Read and process encoding example files
EncodingExamples.encoding_examples_read_and_process()

MyLogger.log_end()

################################################################################
