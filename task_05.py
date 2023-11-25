from random import choices
from task_04 import create_func

"""
Задание №5
✔ Доработаем предыдущую задачу.
✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно.
✔ Внутри используйте вызов функции из прошлой задачи.
"""


def func_new(files=10, **kwargs):
    dct = kwargs
    val = []
    for k, v in dct.items():
        val.append(v)
    for i in range(files):
        ext = str(*choices(val))
        create_func(ext, min_len=6, max_len=30, min_rand_bytes=256, max_rand_bytes=4096, files=1)


if __name__ == '__main__':
    print(func_new(5, a='.txt', b='.doc', c='.dat'))