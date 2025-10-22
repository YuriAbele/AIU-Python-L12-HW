class CONSTANTS:
    
    PATH_DATA_BASE: str = "project_root/data/raw/"
    PATH_DATA_PROCESSED: str = "project_root/data/processed/"

    FILE_NAMES: list[str] = [
        "example_UTF8.txt",
        "example_UTF16.txt",
        "example_ASCII.txt",
        "example_ISO-8859-5.txt",
        "example_Windows-1251.txt",
    ]

    ENCODINGS: list[str] = [
        "UTF-8",
        "UTF-16",
        "ASCII",
        "ISO-8859-5", # Cyrillic
        "Windows-1251", # Cyrillic (russian)
    ]

    CONTENT = """
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
