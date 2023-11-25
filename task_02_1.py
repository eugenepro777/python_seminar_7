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

def generate_pseudonym(file_name, num_pseudonyms):
    def generate_name():
        vowels = "aeiou"
        consonants = "bcdfghjklmnpqrstvwxyz"
        name_length = randint(4, 7)
        name = [choice(string.ascii_uppercase)]
        for _ in range(name_length - 1):
            if len(name) % 2 == 0:
                name.append(choice(vowels))
            else:
                name.append(choice(consonants))
        return ''.join(name)
    pseudonyms = set()
    while len(pseudonyms) < num_pseudonyms:
        pseudonyms.add(generate_name())
    with open(file_name, 'a', encoding='utf-8') as f:
        for pseudonym in pseudonyms:
            f.write(f'{pseudonym.capitalize()}\n')


if __name__ == '__main__':
    file_name = 'pseudonyms_list.txt'
    num_pseudonyms = 7
    generate_pseudonym(file_name, num_pseudonyms)

