import os
from os.path import join, getsize

def get_info_files(main_folder):#Возвращает путь,имена и размер всех фаилов в этой директории
    roots = []; names = []; sizes=[]
    for root ,dirs, files in os.walk(main_folder): 
        for file in files:
            roots.append(root)
            names.append(file)
            sizes.append(getsize(join(root, file)))
    return roots,names,sizes


def are_files_duplicates(roots, names, sizes):#Ищет дубликаты,возвращает найденные
    overlooked = []
    duplicates = []
    for file_1 in range(len(names)):
        for file_2 in range(len(names)):
            if (file_1 != file_2) and (overlooked.count(file_1) == 0) and (overlooked.count(file_1) == 0) and (names[file_1] == names[file_2]) and (sizes[file_1] == sizes[file_2]):
                overlooked.append(file_1)
                overlooked.append(file_2)
                duplicates.append([file_2, file_1])
    return duplicates

def print_result(duplicates,roots, names, sizes):
    for file in duplicates:
        print('Файл с именем %s, размером %dкб, находящийся в директории %s' % (names[file[0]], sizes[file[0]], join(roots[file[0]], names[file[0]])))
        print('является дубликатом файла с именем %s, размером %dкб, находящимся в директории %s' % (names[file[1]], sizes[file[1]], join(roots[file[1]], names[file[1]])))
        print('----------------------------------------------------------------------------------------------')

        
    
if __name__ == '__main__':
    path_name = input("Введите путь до директории,для поиска похожих фаилов:  ")
    files_info = get_info_files(path_name)
    duplicates = are_files_duplicates(*files_info)
    if duplicates:
        print_result(duplicates, *files_info)
    else:
        print("Дубликатов необнаружено")
    
