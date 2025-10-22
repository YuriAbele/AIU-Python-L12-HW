import chardet
import _CONSTANTS as CONSTANTS
from _filesystem_helper import FileSystemHelper
from _logging_helper import LoggingHelper

class EncodingExamples:
   
        
    @staticmethod
    def encoding_examples_generate() -> None:
        """
        Generate text files with different encodings for testing purposes.
        """
        
        LoggingHelper.info("\nGenerating encoding example files:START")
        
        for file_name, encoding in zip(CONSTANTS.FILE_NAMES, CONSTANTS.ENCODING_NAMES):
            full_path = FileSystemHelper.calc_file_full_path(CONSTANTS.BASE_PATH_DATA_RAW, file_name)
            LoggingHelper.debug(f"--> Create or replace the \"{full_path}\" file with \"{encoding}\" encoding.")
            with open(full_path, 'w', encoding=encoding, errors='replace') as f:
                f.write(CONSTANTS.EXAMPLE_CONTENT)
                
        LoggingHelper.info("Generating encoding example files:END")
        
    # Read auto-generated text files with different encodings and autodetect their encodings
    @staticmethod
    def encoding_examples_read_and_process() -> None:
        """
        Read auto-generated text files with different encodings and autodetect their encodings.
        """

        LoggingHelper.info("\nReading encoding example files:START")

        for file_name in CONSTANTS.FILE_NAMES:
            LoggingHelper.debug(f"--> Processing file: {file_name}")
            full_path_raw = FileSystemHelper.calc_file_full_path(CONSTANTS.BASE_PATH_DATA_RAW, file_name)
            full_path_processed = FileSystemHelper.calc_file_full_path(CONSTANTS.BASE_PATH_DATA_PROCESSED, file_name, suffix="_processed")
            LoggingHelper.debug(f"\t--> Read the \"{full_path_raw}\" file.")
            with open(full_path_raw, 'rb') as input_file:
                content_bytes = input_file.read()
                encoding_detected = chardet.detect(content_bytes)
                encoding_detected_name = encoding_detected["encoding"] if encoding_detected["encoding"] is not None else "utf-8" # Fallback to utf-8 if detection fails
                LoggingHelper.debug(f"\t--> Detected encoding for \"{full_path_raw}\": {encoding_detected_name} with confidence {encoding_detected['confidence']:.2f}")
                content_decoded = content_bytes.decode(encoding=encoding_detected_name, errors='replace')
                
                content_decoded_swapped = content_decoded.swapcase()
                # IMPORTANT: Because we read the file in binary mode, we need to write it back in text mode with newline='' to avoid adding extra newlines on Windows
                with open(full_path_processed, 'w', encoding=encoding_detected_name, errors='replace', newline='') as output_file:
                    LoggingHelper.debug(f"\t--> Write the processed content to \"{full_path_processed}\" file.")
                    output_file.write(content_decoded_swapped)

        LoggingHelper.info("Reading encoding example files:END")
