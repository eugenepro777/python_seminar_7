from math import floor

"""
Задание №3
✔ Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
✔ если результат умножения отрицательный, сохраните имя
записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя
прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк,
сколько в более длинном файле.
✔ При достижении конца более короткого файла,
возвращайтесь в его начало.
"""


def read_files(file_name):
    with (
        open('task_2_test.txt', 'r', encoding='utf-8') as f1,
        open('test_func.txt', 'r', encoding='utf-8') as f2,
        open(file_name, 'w', encoding='utf-8') as f3
    ):
        names_list = list(f1)
        nums_list = list(f2)
        max_len = max(len(names_list), len(nums_list))
        names_final, nums_final = [], []
        for i in range(max_len):
            name = names_list[i % len(names_list)].strip()
            num = int(nums_list[i % len(nums_list)].split(' | ')[0]) * \
                  float(nums_list[i % len(nums_list)].split(' | ')[1])
            if num >= 0:
                print(f'{name.upper()} - {floor(num)}', file=f3)
            else:
                print(f'{name.lower()} - {abs(num)}', file=f3)


if __name__ == '__main__':
    read_files('task_3_test.txt')