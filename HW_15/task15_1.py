import os
import logging
from collections import namedtuple
import argparse

logging.basicConfig(filename='log.txt', level=logging.DEBUG)

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'flag', 'parent'])

def get_contents(path):
    try:
        contents = []
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isfile(item_path):
                name, extension = os.path.splitext(item)
                contents.append(FileInfo(name, extension, False, path))
            elif os.path.isdir(item_path):
                contents.append(FileInfo(item, None, True, os.path.abspath(os.path.join(path, os.pardir))))
        logging.info('Получен контент')
        return contents
    except Exception as e:
        logging.exception(f"Обнаружена ошибка: {e}")

def save(contents):
    try:
        with open('contents.txt', 'w') as file:
            for item in contents:
                file.write(f"Имя: {item.name}\n")
                if item.extension:
                    file.write(f"Расширение: {item.extension}\n")
                file.write(f"Флаг каталога: {item.flag}\n")
                file.write(f"Название родительского каталога: {item.parent}\n\n")
        logging.info('Выполнено сохранение')
    except Exception as e:
        logging.exception(f"Обнаружена ошибка: {e}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help="Путь к директории", nargs="?", type=str, default=".")
    args = parser.parse_args()
    contents = get_contents(args.path)
    save(contents)

if __name__ == "__main__":
    main()
    logging.shutdown()
    input("\nНажмите ENTER для выхода из программы")


# python .\task15_1.py C:\Users\Ольга\Desktop\Exeptions_DZ\Exeptions_DZ