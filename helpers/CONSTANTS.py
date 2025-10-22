#class CONSTANTS:

BASE_PATH_ROOT: str = "project_root"
BASE_PATH_LOGS: str = f"{BASE_PATH_ROOT}/logs"
BASE_PATH_DATA: str = f"{BASE_PATH_ROOT}/data"
BASE_PATH_DATA_RAW: str = f"{BASE_PATH_DATA}/raw"
BASE_PATH_DATA_PROCESSED: str = f"{BASE_PATH_DATA}/processed"
BASE_PATH_OUTPUT: str = f"{BASE_PATH_ROOT}/output"
BASE_PATH_BACKUPS: str = f"{BASE_PATH_ROOT}/backups"

BASE_FILE_NAME_BACKUP: str = "backup"

FILE_NAME_LOG: str = "app.log"
FILE_NAME_JSON_OUTPUT: str = "processed_data.json"

FS_STRUCTURE = [
    BASE_PATH_ROOT, # root directory
    BASE_PATH_LOGS,
    BASE_PATH_DATA,
    BASE_PATH_DATA_RAW,
    BASE_PATH_DATA_PROCESSED,
    BASE_PATH_OUTPUT,
    BASE_PATH_BACKUPS,
]

FILE_NAMES: list[str] = [
    "example_UTF8.txt",
    "example_UTF16.txt",
    "example_ASCII.txt",
    "example_ISO-8859-5.txt",
    "example_Windows-1251.txt",
]

ENCODING_NAMES: list[str] = [
    "UTF-8",
    "UTF-16",
    "ASCII",
    "ISO-8859-5", # Cyrillic
    "Windows-1251", # Cyrillic (russian)
]

EXAMPLE_CONTENT = """
[LATIN TEXT]
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Далеко-далеко за словесными горами в стране гласных и согласных живут рыбные тексты.

[РУССКИЙ ТЕКСТ]
Вдали от всех живут они в буквенных домах на берегу Семантика большого языкового океана.
Маленький ручеек Даль журчит по всей стране и обеспечивает ее всеми необходимыми правилами.
Прямо в сердце страны гласных и согласных есть маленький ручеек, который называется Даль.
Он течет по всей стране и обеспечивает ее всеми необходимыми правилами.

[SPECIAL CHARACTERS]
!@#$%^&*()_+-=[]{}|;':",.<>/?`~ ¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ ÐðÞþÆæŒœŠšŸÿ
    """.strip()
