from random import randint, uniform
"""
Задание №1
✔ Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.
"""


def digit_generate(number_lines, filename):
    with open(filename, 'a+', encoding='utf-8') as f:
        for _ in range(0, number_lines):
            first_digit = randint(-1000, 1000)
            second_digit = uniform(-1000, 1000)
            f.write(f'{first_digit} | {second_digit:.2f}\n')


file_name = 'test_func.txt'
digit_generate(7, file_name)