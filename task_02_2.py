from random import randint, choice

"""
Задание №2
✔ Напишите функцию, которая генерирует
псевдоимена.
✔ Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.
"""


def pseudonym_generate(num_lines, filename):
    pseudonyms = set()

    while len(pseudonyms) < num_lines:
        name_length = randint(4, 7)
        name = [choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')]
        vowels = "AEIOU"
        consonants = "BCDFGHJKLMNPQRSTVWXYZ"
        for _ in range(name_length - 1):
            if len(name) % 2 == 0:
                name.append(choice(vowels))
            else:
                name.append(choice(consonants))
        pseudonym = ''.join(name)
        pseudonyms.add(pseudonym)
    with open(filename, 'a', encoding='utf-8') as f:
        for pseudonym in pseudonyms:
            f.write(f'{pseudonym.capitalize()}\n')


if __name__ == '__main__':
    file_name = "pseudonyms_list.txt"
    num_pseudonyms = 10
    pseudonym_generate(num_pseudonyms, file_name)