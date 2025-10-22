import os
from datetime import datetime
import logging
from colorama import Fore, Back, Style, init as colorama_init
from pathlib import Path

import _CONSTANTS as CONSTANTS

class MyLogger:
    __SPLIT_LINE: str = "#" * 100
    
    def __init__(self) -> None:
        pass

    @staticmethod
    def log_start():
        # Initialize colorama for colored console output
        colorama_init(autoreset=True)
        
        # We will use root logger and root logger configuration
        logging.basicConfig(
            filename=os.path.join(CONSTANTS.BASE_PATH_LOGS, CONSTANTS.FILE_NAME_LOG), # Имя файла
            filemode='w',       # 'w' - перезаписать, 'a' - добавить (по умолчанию)
            format='%(asctime)s - %(levelname)s - %(message)s',
            level=logging.DEBUG,
            datefmt='%Y-%m-%d %H:%M:%S')

        logging.info(f"STARTED {MyLogger.__SPLIT_LINE}")
        print(Fore.LIGHTYELLOW_EX + f"\n{"="*50}\nStarted at: {datetime.now():%Y-%m-%d %H:%M:%S}\n{MyLogger.__SPLIT_LINE}")


    @staticmethod
    def display_tree(directory: Path, prefix: str = "", is_root: bool = True) -> None:
        """
        Recursively displays the directory and file tree.
        """

        if is_root:
            MyLogger.debug(f"{directory}/".replace("\\", "/"))

        # Get the list of contents, ignoring "hidden" files/folders
        # (optionally, you can remove startswith('.'))
        items = [p for p in directory.iterdir() if not p.name.startswith('.')]
        
        # Sort for order
        items.sort()

        # Prepare "pointers"
        pointers = ["├── "] * (len(items) - 1) + ["└── "]

        for pointer, path in zip(pointers, items):
            # Print the current item
            MyLogger.debug(f"{prefix}{pointer}{path.name}")
            
            # If it is a directory, recursively call it for it.
            if path.is_dir():
                # Determine what prefix to pass "deeper"
                extension = "│   " if pointer == "├── " else "    "
                MyLogger.display_tree(path, prefix=prefix + extension, is_root=False)
    
    @staticmethod
    def log_end():
        logging.info(f"FINISHED {MyLogger.__SPLIT_LINE}")
        print(Fore.LIGHTYELLOW_EX + f"\n{MyLogger.__SPLIT_LINE}\nFinished at: {datetime.now():%Y-%m-%d %H:%M:%S}\n{"="*50}\n")
        
    @staticmethod
    def print_split_line():
        print(Fore.LIGHTYELLOW_EX + "\n" + MyLogger.__SPLIT_LINE)
        
    @staticmethod
    def debug(message: str):
        print(Fore.GREEN + message)
        logging.debug(message.strip())
        
    @staticmethod
    def info(message: str):
        print(Fore.LIGHTWHITE_EX + message)
        logging.info(message.strip())
        
    @staticmethod
    def error(message: str):
        print(Fore.RED + message)
        logging.error(message.strip())

    @staticmethod
    def tests():
        MyLogger.log_start()
        MyLogger.print_split_line()
        MyLogger.info("This is an INFO message.")
        MyLogger.debug("This is a DEBUG message.")
        MyLogger.error("This is an ERROR message.")
        MyLogger.log_end()
