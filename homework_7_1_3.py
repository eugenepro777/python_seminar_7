import os

"""
Задание 1
Напишите функцию группового переименования файлов в папке test_folder под названием rename_files. Она должна:

a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
f. Папка test_folder доступна из текущей директории

# Создать тестовую папку
folder_name = "test_folder"
folder_path = os.path.join(os.getcwd(), folder_name)
if os.path.exists(folder_path):
    shutil.rmtree(folder_path)
os.makedirs(folder_path)

# # Заполнить тестовую папку
file_name = "test1.txt"
file_path = os.path.join(folder_path, file_name)
with open(file_path, "w") as file:
    file.write("This is a test file.\n")
    file.close()

# Заполнить тестовую папку
for i in range(10):

    file_name = f"test{i}.txt"
    file_path = os.path.join(folder_path, file_name)

    with open(file_path, "w") as file:
        file.write("This is a test file.\n")
        file.close()

file_name = "test.doc"
file_path = os.path.join(folder_path, file_name)

with open(file_path, "w") as file:
    file.write("This is a test file.\n")
    file.close()

"""
# РАБОЧИЙ ВАРИАНТ


def rename_files(desired_name="", num_digits=0, source_ext="", target_ext="", origin_name_d=None):
    folder = 'test_folder'
    path = os.path.join(os.getcwd(), folder)
    counter = 1
    # new_name = ''

    for file in os.listdir(path):
        extension = os.path.splitext(file)[1].lower().replace('.', '')
        old_file_name = os.path.splitext(file)[0].lower()

        if extension == source_ext:
            str_num = '0' * (num_digits - len(str(counter))) + str(counter)

            new_name = desired_name + str_num + '.' + target_ext

            os.rename(os.path.join(path, file), os.path.join(path, new_name))
            counter += 1
    # print(*os.listdir(path))




# 1
rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")


"""
Задание 2
"""
# with open('__init__.py', 'w', encoding='utf-8') as file:
#     file.writelines('def rename_files():\n')