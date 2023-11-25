import os

"""
Задание №7

✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""


def sort_files(dir):
    folders = {}
    folders['Video'] = ['.mp4', '.avi', '.mkv']
    folders['Pictures'] = ['.png', '.jpg', '.jpeg', '.gif', '.tiff']
    folders['Texts'] = ['.txt', '.rtf', '.doc', '.docx', '.pdf']
    if not os.path.exists(dir):
        print('Указанная директория не существует')
    else:
        for dir, _, files in os.walk(dir):
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                path = os.path.join(dir, file)
                for k, v in folders.items():
                    if ext in v:
                        if not os.path.exists(os.path.join(dir, k)):
                            os.mkdir(os.path.join(dir, k))
                        new_path = os.path.join(dir, k, file)
                        os.replace(path, new_path)


if __name__ == '__main__':
    sort_files('F:\Python\python_seminar_7\\')
