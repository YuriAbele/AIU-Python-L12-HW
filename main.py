from _init_logging import MyLogger
from _ensure_fs_structure import ensure_fs_structure
from _encoding_examples import generate_encoding_examples

################################################################################

MyLogger.log_start()

ensure_fs_structure()
generate_encoding_examples()

MyLogger.log_end()

################################################################################
