import os
from random import choice, randint
import string

"""
Задание №5
✔ Доработаем предыдущую задачу.
✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно.
✔ Внутри используйте вызов функции из прошлой задачи.
"""


def create_files(ext, min_name=6, max_name=30, min_bytes=256, max_bytes=4096, files=42):
    if files <= 0:
        return

    min_name = max(1, min_name)
    max_name = max(min_name, max_name)
    min_bytes = max(1, min_bytes)
    max_bytes = max(min_bytes, max_bytes)

    if not os.path.exists(ext):
        os.mkdir(ext)

    for _ in range(files):
        file_name = ''.join(choice(string.ascii_letters + string.digits) for _ in range(randint(min_name, max_name))) \
                    + f'.{ext}'
        file_content = os.urandom(randint(min_bytes, max_bytes))

        with open(os.path.join(ext, file_name), 'wb') as f:
            f.write(file_content)


def generate_files(ext_list, files_list):
    for extension, file in zip(ext_list, files_list):
        create_files(extension, files=file)


extensions = ["txt", "csv", "dat", "rtf"]
num_files = [7, 4, 9, 2]

generate_files(extensions, num_files)