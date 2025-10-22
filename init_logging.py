from datetime import datetime
import logging
from colorama import Fore, Back, Style, init as colorama_init

class MyLogger:
    __SPLIT_LINE = "#" * 100
    
    def __init__(self) -> None:
        pass

    @staticmethod
    def log_start():
        # Initialize colorama for colored console output
        colorama_init(autoreset=True)
        
        # We will use root logger and root logger configuration
        logging.basicConfig(
            filename='project_root/logs/app.log', # Имя файла
            filemode='w',       # 'w' - перезаписать, 'a' - добавить (по умолчанию)
            format='%(asctime)s - %(levelname)s - %(message)s',
            level=logging.DEBUG,
            datefmt='%Y-%m-%d %H:%M:%S')

        logging.info(f"STARTED {MyLogger.__SPLIT_LINE}")
        print(f"\n{"="*50}\nStarted at: {datetime.now():%Y-%m-%d %H:%M:%S}{MyLogger.__SPLIT_LINE}")
    
    @staticmethod
    def log_end():
        logging.info(f"FINISHED {MyLogger.__SPLIT_LINE}")
        print(f"\n{MyLogger.__SPLIT_LINE}\nFinished at: {datetime.now():%Y-%m-%d %H:%M:%S}\n{"="*50}\n")
        
    @staticmethod
    def print_split_line():
        print(Style.DIM + MyLogger.__SPLIT_LINE)
        
    @staticmethod
    def debug(message: str):
        print(Fore.GREEN + message)
        logging.debug(message)
        
    @staticmethod
    def info(message: str):
        print(message)
        logging.info(message)
        
    @staticmethod
    def error(message: str):
        print(Fore.RED + message)
        logging.error(message)
        
MyLogger.log_start()

MyLogger.print_split_line()

MyLogger.info("This is an info message.")
MyLogger.debug("This is a debug message.")
MyLogger.error("This is an error message.")

MyLogger.log_end()