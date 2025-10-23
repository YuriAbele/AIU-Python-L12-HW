# AIU-Python-L12-HW
Python-разработчик | #12 | Работа с файлами, с операционной системой и путями. Кодировки, сериализация данных, json

# Отчёт о выполнении

## 0. Общие замечания. Общая информация.

- Всё опубликовано в GitHub в public GIT Repository с [множеством comit-ов](https://github.com/YuriAbele/AIU-Python-L12-HW/commits/main/)
- проект содержит [**``.gitignore``**](./.gitignore) настроенный для **``Python``**
- Все макрометоды содержат для отладки сообщение о старте и окончании, а так же какие-то промежуточные сообщения. Пример вывода в терминал:<br/>
  ![Screenshot example terminal](./Screenshot_example_terminal.png)
-  Вся работа всего решения выводится в консоль и записывается в лог файл [**``./project_root/logs/app.log``**](https://github.com/YuriAbele/AIU-Python-L12-HW/blob/main/project_root/logs/app.log)<br/>
  VSCode показывает этот лог более красочно:<br/>
  ![Screenshot example app.log](./Screenshot_example_app_log.png)

### 0.1. Суммарно во всём проекте использованные пакеты:

```python
import os
from pathlib import Path
import shutil
from datetime import datetime
import chardet
import hashlib
import json
from jsonschema import validate, ValidationError
import logging
from colorama import Fore, Back, Style, init as colorama_init
```


### 0.2 Был создан helpers пакет со своим __init__.py. В этом пакете хэлперы:

- **``CONSTANTS.py``** - это не хэлпер а файл с константами, чтобы:
    - избежать **<i>"magic constants"</i>**
    - соблюсти принцип **SPOT** (**S**ingle **P**oint **o**f **T**ruth)

- **``LoggingHelper``**
    - для упрощения вывода сообщения отладки в терминал<br/>и<br/>параллельно в лог файл **``./project_root/logs/app.log``**
    - по факту использованы все уровни логгирования
        - DEBUG, INFO, WARN и ERROR
    - выводит для отладки содержимое файла
    - выводит для отладки структуру дерева папок и файлов

- **``FileSystemHelper``**
    - гарантиует структуру папки **``project_root``**
    - макрометоды для вычисления полных путей
    - методы для очистки file-system структур
    - сбор метаинформации о дереве файлов
    - считывает файл как строку
    - сохранение текста в файл
    - подсчёт хэша файлов

- **``BackupHelper``**
    - архивирует папку **``./project_root/data``**
    - ищет последний созданный бэкап
    - восстанавливает папку **``./project_root/data``**

- **``SerializationHelper``**
    - использует созданный в том же модуле класс **``FilesPairData``** - нужен для примеров с кодировками
    - методы для считывания пар файлов (разных кодировок) до и после processing в список **``FilesPairData``**
    - сериализация списка в JSON строку
    - десериализация JSON массива (строки) в **``list[FileInfo]``**
    - сравнение двух **``list[FileInfo]``**
    - считывание файла с JSON Schema в соотв. **``dict``**
    - валидация JSON строки в соотв. с **``dict``** JSON схемой

и наконец:

- **``EncodingExamples``**
    - генерирует тестовые файлы в разных кодировках в папку **``./project_root/data/raw``**
    - считывает сгенерённые файлы и сохраняет преобразованные (**``Swap-Case``**) в папку **``./project_root/data/processed``**

----
----
----

## 1. Управление проектной структурой и файловой системой

### 1.1. Создание и управление директориями



### 1.2. Создание и запись данных в файлы