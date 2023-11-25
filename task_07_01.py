import os
import shutil

"""
Задание №7
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""


def sorting_file_types(source, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)

    for filename in os.listdir(source):
        source_path = os.path.join(source, filename)

        if os.path.isfile(source_path):
            extension = filename.split('.')[-1].lower()
            dest_subdir = None

            if extension in ['mp4', 'avi', 'mkv', 'wmv', 'mov']:
                dest_subdir = 'videos'
            elif extension in ['jpg', 'jpeg', 'png', 'gif']:
                dest_subdir = 'images'
            elif extension in ['txt', 'pdf', 'rtf', 'doc', 'docx', 'csv']:
                dest_subdir = 'text'
            else:
                # Если файл не соответствует заданным типам, то оставить его в исходной директории
                continue

            dest_subdir_path = os.path.join(destination, dest_subdir)
            if not os.path.exists(dest_subdir_path):
                os.makedirs(dest_subdir_path)
            dest_path = os.path.join(dest_subdir_path, filename)

            shutil.move(source_path, dest_path)


source = "dir/subdir/source"
destination = "dir/subdir/destination"