import os
import chardet
from _CONSTANTS import CONSTANTS
from _init_logging import MyLogger

class EncodingExamples:
   
    @staticmethod
    def clean_target_files() -> None:
        """
        Clean up previously generated encoding example files.
        """
        
        MyLogger.info("\nCleaning encoding example files:START")
        
        for filename in os.listdir(CONSTANTS.PATH_DATA_BASE):
            full_path = os.path.join(CONSTANTS.PATH_DATA_BASE, filename)
            if os.path.isfile(full_path):
                MyLogger.debug(f"--> Remove the \"{full_path}\" file.")
                os.remove(full_path)
        for filename in os.listdir(CONSTANTS.PATH_DATA_PROCESSED):
            full_path = os.path.join(CONSTANTS.PATH_DATA_PROCESSED, filename)
            if os.path.isfile(full_path):
                MyLogger.debug(f"--> Remove the \"{full_path}\" file.")
                os.remove(full_path)
                
        MyLogger.info("Cleaning encoding example files:END")
        
    @staticmethod
    def encoding_examples_generate() -> None:
        """
        Generate text files with different encodings for testing purposes.
        """
        
        MyLogger.info("\nGenerating encoding example files:START")
        
        for filename, encoding in zip(CONSTANTS.FILE_NAMES, CONSTANTS.ENCODINGS):
            full_path = os.path.join(CONSTANTS.PATH_DATA_BASE, filename)
            MyLogger.debug(f"--> Create or replace the \"{full_path}\" file with \"{encoding}\" encoding.")
            with open(full_path, 'w', encoding=encoding, errors='replace') as f:
                f.write(CONSTANTS.CONTENT)
                
        MyLogger.info("Generating encoding example files:END")
        
    # Read auto-generated text files with different encodings and autodetect their encodings
    @staticmethod
    def encoding_examples_read_and_process() -> None:
        """
        Read auto-generated text files with different encodings and autodetect their encodings.
        """

        MyLogger.info("\nReading encoding example files:START")

        for filename in CONSTANTS.FILE_NAMES:
            MyLogger.debug(f"--> Processing file: {filename}")
            full_path_input = os.path.join(CONSTANTS.PATH_DATA_BASE, filename)
            full_path_output = os.path.join(CONSTANTS.PATH_DATA_PROCESSED, filename).split('.')[0] + "_processed." + filename.split('.')[-1] # Append "_processed" to the filename before the extension
            MyLogger.debug(f"\t--> Read the \"{full_path_input}\" file.")
            with open(full_path_input, 'rb') as input_file:
                content_bytes = input_file.read()
                encoding_detected = chardet.detect(content_bytes)
                encoding_detected_name = encoding_detected["encoding"] if encoding_detected["encoding"] is not None else "utf-8" # Fallback to utf-8 if detection fails
                MyLogger.debug(f"\t--> Detected encoding for \"{full_path_input}\": {encoding_detected_name} with confidence {encoding_detected['confidence']:.2f}")
                content_decoded = content_bytes.decode(encoding=encoding_detected_name, errors='replace')
                
                content_decoded_swapped = content_decoded.swapcase()
                # IMPORTANT: Because we read the file in binary mode, we need to write it back in text mode with newline='' to avoid adding extra newlines on Windows
                with open(full_path_output, 'w', encoding=encoding_detected_name, errors='replace', newline='') as output_file:
                    MyLogger.debug(f"\t--> Write the processed content to \"{full_path_output}\" file.")
                    output_file.write(content_decoded_swapped)

        MyLogger.info("Reading encoding example files:END")
