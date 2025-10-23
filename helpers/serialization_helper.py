from datetime import datetime
import json
import os

from helpers.file_info import FileInfo

from . import CONSTANTS as CONSTANTS
from .logging_helper import LoggingHelper
from .filesystem_helper import FileSystemHelper
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

class SerializationHelper:

    @staticmethod
    def read_many_files() -> list[FilesPairData]:
        """
        Read multiple text files from the base data directory and return their contents as a list of FilesPairData.
        """
        
        LoggingHelper.info("\nRead many files:START")
        
        output_list: list[FilesPairData] = []
        for (file_name, encoding_name) in zip(CONSTANTS.FILE_NAMES, CONSTANTS.ENCODING_NAMES):
            file_pair_data = SerializationHelper.read_filepair_data(file_name, encoding_name=encoding_name)
            # file_data_dict = file_data.to_dict()
            output_list.append(file_pair_data)

        LoggingHelper.info("Read many files:END")
        return output_list

    @staticmethod
    def read_filepair_data(file_name: str, encoding_name: str) -> FilesPairData:
        """
        Read a pair of text files (raw and processed), using the specified encoding, and return a FileData object.
        """
        LoggingHelper.info(f"\tProcess file_name \"{file_name}\":START")

        # Construct full file paths
        full_path_raw = FileSystemHelper.calc_file_full_path(CONSTANTS.BASE_PATH_DATA_RAW, file_name)
        full_path_processed = FileSystemHelper.calc_file_full_path(CONSTANTS.BASE_PATH_DATA_PROCESSED, file_name, suffix="_processed")

        file_data: FilesPairData = FilesPairData(file_name = file_name, encoding_name = encoding_name)
        
        # Get raw file size and last modified timestamp
        file_data.size = os.path.getsize(full_path_raw)
        file_data.last_modified_at = datetime.fromtimestamp(os.path.getmtime(full_path_raw)).strftime("%Y-%m-%d %H:%M:%S")

        # Read the raw file
        with open(full_path_raw, 'r', encoding=encoding_name) as input_file:
            file_data.content_raw = input_file.read()
            LoggingHelper.debug(f"\t\t--> Read {len(file_data.content_raw)} characters from \"{full_path_raw}\" file.")

        # Read the processed file
        with open(full_path_processed, 'r', encoding=encoding_name) as input_file:
            file_data.content_processed = input_file.read()
            LoggingHelper.debug(f"\t\t--> Read {len(file_data.content_processed)} characters from \"{full_path_processed}\" file.")

        LoggingHelper.info(f"\tProcess file_name \"{file_name}\":END")
        return file_data
        
    @staticmethod
    def serialize_list_to_json_array(source_list: list) -> str:
        """
        Convert a list of FilesPairData to a JSON string.
        """
        
        list_size = len(source_list)
        LoggingHelper.info(f"\nConvert a list to a JSON array:START")
        
        output_json = json.dumps(source_list, default=lambda o: o.__dict__, indent=4)
        LoggingHelper.debug(f"\t--> Got {len(output_json)} characters")

        LoggingHelper.info(f"Convert a list to a JSON array:END")
        return output_json
        
    @staticmethod
    def save_json_to_file(json_string: str, output_path: str) -> None:
        """
        Save the JSON string to a file.
        """

        LoggingHelper.info("\nSaving JSON to file:START")
        
        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_size = output_file.write(json_string)
            LoggingHelper.debug(f"\t--> Saved {output_size} bytes to \"{output_path}\" file.")

        LoggingHelper.info("Saving JSON to file:END")

    @staticmethod
    def deserialize_json_array_to_fileinfo_list(json_string: str) -> list[FileInfo]:
        """
        Convert a JSON string to a list of FileInfo objects.
        """
        
        LoggingHelper.info(f"\nConvert a JSON array to a list:START")
        
        data_list = json.loads(json_string)
        output_list: list[FileInfo] = []
        for item in data_list:
            file_info = FileInfo(
                file_name=item.get('file_name'),
                full_path=item.get('full_path'),
                size=item.get('size'),
                last_modified_at=item.get('last_modified_at'),
                hash=item.get('hash'),
            )
            output_list.append(file_info)
        
        LoggingHelper.debug(f"\t--> Got {len(output_list)} FileInfo objects")

        LoggingHelper.info(f"Convert a JSON array to a list:END")
        return output_list
    
    @staticmethod
    def compare_fileinfo_lists(list1: list[FileInfo], list2: list[FileInfo]) -> bool:
        """
        Compare two lists of FileInfo objects for equality.
        """
        
        LoggingHelper.info(f"\nCompare file info lists:START")

        if len(list1) != len(list2):
            return False
        LoggingHelper.debug(f"\t--> Both lists have {len(list1)} items")
        
        for fi1, fi2 in zip(list1, list2):
            if fi1.file_name != fi2.file_name or fi1.full_path != fi2.full_path or fi1.size != fi2.size or fi1.last_modified_at != fi2.last_modified_at:
                return False
        LoggingHelper.debug(f"\t--> Both lists are identical")
            
        LoggingHelper.info(f"Compare file info lists:END")
        return True
