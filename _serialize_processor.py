from datetime import datetime
import json
import os
from _CONSTANTS import CONSTANTS
from _fs_helper import FileSystemHelper
from _init_logging import MyLogger

class FilesPairData:
    def __init__(self,
                 file_name: str | None = None,
                 encoding_name: str | None = None,
                 content_raw: str | None = None,
                 content_processed: str | None = None,
                 size: int | None = None,
                 last_modified_at: str | None = None) -> None:
        self.file_name = file_name
        self.encoding_name = encoding_name
        self.content_raw = content_raw
        self.content_processed = content_processed
        self.size = size
        self.last_modified_at = last_modified_at

class SerializeProcessor:

    @staticmethod
    def read_many_files() -> list[FilesPairData]:
        """
        Read multiple text files from the base data directory and return their contents as a list of FilesPairData.
        """
        
        MyLogger.info("\nRead many files:START")
        
        output_list: list[FilesPairData] = []
        for (file_name, encoding_name) in zip(CONSTANTS.FILE_NAMES, CONSTANTS.ENCODING_NAMES):
            file_pair_data = SerializeProcessor.read_filepair_data(file_name, encoding_name=encoding_name)
            # file_data_dict = file_data.to_dict()
            output_list.append(file_pair_data)

        MyLogger.info("Read many files:END")
        return output_list

    @staticmethod
    def read_filepair_data(file_name: str, encoding_name: str) -> FilesPairData:
        """
        Read a pair of text files (raw and processed), using the specified encoding, and return a FileData object.
        """
        MyLogger.info(f"\tProcess file_name \"{file_name}\":START")

        # Construct full file paths
        full_path_raw = FileSystemHelper.calc_file_full_path(CONSTANTS.PATH_DATA_RAW, file_name)
        full_path_processed = FileSystemHelper.calc_file_full_path(CONSTANTS.PATH_DATA_PROCESSED, file_name, suffix="_processed")

        file_data: FilesPairData = FilesPairData(file_name = file_name, encoding_name = encoding_name)
        
        # Get raw file size and last modified timestamp
        file_data.size = os.path.getsize(full_path_raw)
        file_data.last_modified_at = datetime.fromtimestamp(os.path.getmtime(full_path_raw)).strftime("%Y-%m-%d %H:%M:%S")

        # Read the raw file
        with open(full_path_raw, 'r', encoding=encoding_name) as input_file:
            file_data.content_raw = input_file.read()
            MyLogger.debug(f"\t\t--> Read {len(file_data.content_raw)} characters from \"{full_path_raw}\" file.")

        # Read the processed file
        with open(full_path_processed, 'r', encoding=encoding_name) as input_file:
            file_data.content_processed = input_file.read()
            MyLogger.debug(f"\t\t--> Read {len(file_data.content_processed)} characters from \"{full_path_processed}\" file.")

        MyLogger.info(f"\tProcess file_name \"{file_name}\":END")
        return file_data
        
    @staticmethod
    def serialize_to_json(source_list: list[FilesPairData]) -> str:
        """
        Convert a list of FilesPairData to a JSON string.
        """
        
        list_size = len(source_list)
        MyLogger.info(f"\nConvert a list of {list_size} FilesPairData items to a JSON:START")
        
        output_json = json.dumps(source_list, default=lambda o: o.__dict__, indent=4)
        MyLogger.debug(f"\t--> Got {len(output_json)} characters")

        MyLogger.info(f"Convert a list of {list_size} FilesPairData items to a JSON:END")
        return output_json
        
    @staticmethod
    def save_json_to_file(json_string: str) -> None:
        """
        Save the JSON string to a file.
        """

        MyLogger.info("\nSaving JSON to file:START")

        output_path = os.path.join(CONSTANTS.PATH_OUTPUT, "encoded_examples.json")
        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_size = output_file.write(json_string)
            MyLogger.debug(f"\t--> Saved {output_size} bytes to \"{output_path}\" file.")

        MyLogger.info("Saving JSON to file:END")
