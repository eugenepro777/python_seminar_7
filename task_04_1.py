import os
from random import choice, randint
import string

"""
Задание №4
✔ Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.
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


create_files('txt', 6, 15, 512, 2048, 10)
