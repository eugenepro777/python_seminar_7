import os

"""
Напишите функцию группового переименования файлов в папке test_folder под названием rename_files. Она должна:

a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
f. Папка test_folder доступна из текущей директории
"""


def rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc", name_range=None,
                 test_folder=None):
    if name_range is None:
        name_range = (0, 0)

    if test_folder is None:
        test_folder = os.getcwd()

    # if len(name_range) != 2 or name_range[0] < 0 or name_range[1] <= name_range[0]:
    #     raise ValueError("Ошибка в имени файла")

    counter = 1  # Инициализировать счетчик для порядковых номеров
    for root, _, files in os.walk(test_folder):
        for filename in files:
            if filename.endswith(f'.{source_ext}'):
                old_name = os.path.splitext(filename)[0]
                # extension = os.path.splitext(filename)[1]

                if name_range != (0, 0):
                    if name_range[1] > len(old_name):
                        name_range = (name_range[0], len(old_name))

                    name_range_str = old_name[name_range[0]:name_range[1]]
                else:
                    name_range_str = ""
                # Создайте новое имя файла с желаемым префиксом, счетчиком и расширением
                new_name = f"{desired_name}{name_range_str}{str(counter).zfill(num_digits)}.{target_ext}"

                old_path = os.path.join(root, filename)
                new_path = os.path.join(root, new_name)

                os.rename(old_path, new_path)

                counter += 1


# 1
rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")

with open('__init__.py', 'w', encoding='utf-8') as file:
    file.writelines('def rename_files():\n')