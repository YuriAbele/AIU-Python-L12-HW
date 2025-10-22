import os
from _init_logging import MyLogger

CONTENT = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    Далеко-далеко за словесными горами в стране гласных и согласных живут рыбные тексты.
    Вдали от всех живут они в буквенных домах на берегу Семантика большого языкового океана.
    Маленький ручеек Даль журчит по всей стране и обеспечивает ее всеми необходимыми правилами.
    Прямо в сердце страны гласных и согласных есть маленький ручеек, который называется Даль.
    Он течет по всей стране и обеспечивает ее всеми необходимыми правилами.
    """
def generate_encoding_examples() -> None:
    """
    Generate text files with different encodings for testing purposes.
    """
    
    BASE_PATH = "project_root/data/raw/"
    
    filenames = [
        "example_utf8.txt",
        "example_utf16.txt",
        "example_ascii.txt",
        "example_latin1.txt"
    ]
    
    encodings = [
        "utf-8",
        "utf-16",
        "ascii",
        "latin-1"
    ]
    
    MyLogger.info("\nGenerating encoding example files:START")
    
    for filename, encoding in zip(filenames, encodings):
        full_path = os.path.join(BASE_PATH, filename)
        MyLogger.debug(f"--> Create or replace the \"{full_path}\" file with \"{encoding}\" encoding.")
        with open(full_path, 'w', encoding=encoding, errors='replace') as f:
            f.write(CONTENT)
            
    MyLogger.info("Generating encoding example files:END")
    