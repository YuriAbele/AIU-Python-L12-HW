from datetime import datetime
import logging
from colorama import Fore, Back, Style, init as colorama_init

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
            filename='project_root/logs/app.log', # Имя файла
            filemode='w',       # 'w' - перезаписать, 'a' - добавить (по умолчанию)
            format='%(asctime)s - %(levelname)s - %(message)s',
            level=logging.DEBUG,
            datefmt='%Y-%m-%d %H:%M:%S')

        logging.info(f"STARTED {MyLogger.__SPLIT_LINE}")
        print(Fore.LIGHTYELLOW_EX + f"\n{"="*50}\nStarted at: {datetime.now():%Y-%m-%d %H:%M:%S}\n{MyLogger.__SPLIT_LINE}")
    
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