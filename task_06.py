from os import makedirs, chdir, getcwd
from random import choices, randbytes, randint
from string import ascii_lowercase
from task_04 import create_func
from task_05 import func_new

"""
Задание №6
✔ Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
"""


def func_new_2(dir):
    my_path = getcwd() + dir
    try:
        makedirs(my_path)
        chdir(my_path)
    except FileExistsError:
        chdir(my_path)

