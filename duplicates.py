import os
from copy import copy


def get_info_files(main_folder):
    paths = []
    names_and_size = []
    for root, dirs, files in os.walk(main_folder):
        for file in files:
            paths.append(root)
            size = os.path.getsize(u'%s/%s' % (root, file))
            names_and_size.append([file, size])
    return paths, names_and_size


def get_files_duplicates(paths, names_and_size):
    duplicates = []
    names_file_to_index = copy(names_and_size)
    for file in names_and_size:
        if names_and_size.count(file) > 1:
            index = names_file_to_index.index(file)
            duplicates.append([names_and_size[index][0], paths[index]])
            names_file_to_index[index] = None
    return duplicates


def print_dublicates(duplicates):
    print_txt = "Имя файла: {name}   Путь к файлу: {root}"
    for duplicate in sorted(duplicates):
            print(print_txt.format(name=duplicate[0], root=duplicate[1]))

if __name__ == '__main__':
    path_name = input("Введите путь до директории,для поиска похожих фаилов: ")
    files_info = get_info_files(path_name)
    duplicates = get_files_duplicates(*files_info)
    if duplicates:
        print_dublicates(duplicates)
    else:
        print("Дубликатов необнаружено")
