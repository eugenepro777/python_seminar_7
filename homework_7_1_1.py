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


def rename_files(desired_name, num_digits, source_ext, target_ext, name_range=(0, 0), test_folder="./test_folder"):
    # Убедитесь, что name_range является допустимым
    if len(name_range) != 2 or name_range[0] < 0 or name_range[1] <= name_range[0]:
        raise ValueError("Invalid name range")

    num = 1
    for root, _, files in os.walk(test_folder):
        for filename in files:
            if filename.endswith(f".{source_ext}"):
                old_name = os.path.splitext(filename)[0]
                extension = os.path.splitext(filename)[1]

                if name_range != (0, 0):
                    if name_range[1] > len(old_name):
                        name_range = (name_range[0], len(old_name))

                    name_range_str = old_name[name_range[0]:name_range[1]]
                else:
                    name_range_str = ""

                new_name = f"{desired_name}{name_range_str}_{str(num).zfill(num_digits)}.{target_ext}"

                old_path = os.path.join(root, filename)
                new_path = os.path.join(root, new_name)

                # Rename the file
                os.rename(old_path, new_path)

                num += 1
