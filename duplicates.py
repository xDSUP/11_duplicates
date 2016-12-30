import os
from copy import copy

print_txt = "Имя файла: {n}   Путь к файлу: {p}"


def get_info_files(main_folder):  
    paths = []
    names_and_size = []
    for root, dirs, files in os.walk(main_folder):
        for file in files:
            paths.append(root)
            names_and_size.append([file, os.path.getsize(root+'\\'+file)])
    return paths, names_and_size


def get_files_duplicates(paths, names_and_size):
    duplicates = []
    names = copy(names_and_size)  # для исключения повторных индексов
    for file in names_and_size:
        if names_and_size.count(file) > 1:
            index = names.index(file)
            duplicates.append([names_and_size[index][0], paths[index]])
            names[index] = None
    return duplicates

if __name__ == '__main__':
    path_name = input("Введите путь до директории,для поиска похожих фаилов: ")
    files_info = get_info_files(path_name) # Вернет пути, имена, размеры
    duplicates = get_files_duplicates(*files_info)  # Вернет инфо по дубликатам
    if duplicates:
        for duplicate in sorted(duplicates):
            print(print_txt.format(n=duplicate[0], p=duplicate[1]))
    else:
        print("Дубликатов необнаружено")
