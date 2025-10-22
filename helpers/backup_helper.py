from datetime import datetime
import os
import shutil
from pathlib import Path

import _CONSTANTS as CONSTANTS
from helpers.filesystem_helper import FileSystemHelper
from helpers.logging_helper import LoggingHelper

class BackupHelper:

    @staticmethod
    def backup_data(full_path_source_directory: str) -> str:
        """
        Create a .ZIP backup of the directory.
        """
        LoggingHelper.info(f"\nCreating backup for \"{full_path_source_directory}\":START")

        current_date_suffix = datetime.now().strftime("_%Y%m%d")
        full_path_target_file = FileSystemHelper.calc_file_full_path(CONSTANTS.BASE_PATH_BACKUPS, CONSTANTS.BASE_FILE_NAME_BACKUP + current_date_suffix)
        archive_format = 'zip'

        shutil.make_archive(full_path_target_file, archive_format, full_path_source_directory)
        backup_size = os.path.getsize(f"{full_path_target_file}.{archive_format}")
        LoggingHelper.debug(f"--> Backup created at \"{full_path_target_file}.{archive_format}\" (Size: {backup_size} bytes)")

        LoggingHelper.info(f"Creating backup for \"{full_path_source_directory}\":END")
        return full_path_target_file
    
    @staticmethod
    def restore_data(full_path_source_backup: str, full_path_target_directory) -> None:
        """
        Restore files from the latest backup.
        """

        LoggingHelper.info(f"\nUnpacking backup \"{full_path_source_backup}\" to \"{full_path_target_directory}\":START")
        
        # Extract the backup
        shutil.unpack_archive(full_path_source_backup, full_path_target_directory, 'zip')

        LoggingHelper.debug(f"--> Restored files:")
        LoggingHelper.display_tree(Path(CONSTANTS.BASE_PATH_DATA))

        LoggingHelper.info(f"Unpacking backup \"{full_path_source_backup}\" to \"{full_path_target_directory}\":END")

    @staticmethod
    def get_last_backup_full_path() -> str:
        """
        Get full path of latest backup file in <full_path_backups_directory>.
        """

        LoggingHelper.info(f"\nGet full path of latest backup file in \"{CONSTANTS.BASE_PATH_BACKUPS}\":START")

        # Find the latest backup file
        backup_files = [f for f in os.listdir(CONSTANTS.BASE_PATH_BACKUPS) if f.startswith(CONSTANTS.BASE_FILE_NAME_BACKUP) and f.endswith('.zip')]
        if not backup_files:
            raise FileNotFoundError("No backup files found.")
        latest_backup_file = max(backup_files) # sort by name (date suffix)
        full_path_latest_backup = FileSystemHelper.calc_file_full_path(CONSTANTS.BASE_PATH_BACKUPS, latest_backup_file)
        LoggingHelper.debug(f"--> Latest backup file found: \"{full_path_latest_backup}\"")

        LoggingHelper.info(f"Get full path of latest backup file in \"{CONSTANTS.BASE_PATH_BACKUPS}\":END")
        return full_path_latest_backup
