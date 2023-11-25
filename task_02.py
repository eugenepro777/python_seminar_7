from random import randint, choice
import string
"""
Задание №2
✔ Напишите функцию, которая генерирует
псевдоимена.
✔ Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.
"""


def name_generate():
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    name_length = randint(4, 7)
    name = [choice(vowels + consonants).upper()]
    for _ in range(name_length - 1):
        name.append(choice(consonants))
    for _ in range((name_length - 1) // 2):
        name[choice(range(1, name_length - 1))] = choice(vowels)
    return ''.join(name)


def save_names(lines_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as f:
        for _ in range(lines_count):
            print(name_generate(), file=f)


if __name__ == '__main__':
    save_names(7, 'task_2_test.txt')