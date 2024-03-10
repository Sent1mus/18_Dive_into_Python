# Напишите функцию группового переименования файлов в папке test_folder под названием rename_files. Она должна:
#
# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6]
# берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя,
# если оно передано. Далее счётчик файлов и расширение.
# f. Папка test_folder доступна из текущей директории

import os
from pathlib import Path


# Решение 1
def rename_files(desired_name, num_digits, source_ext, target_ext):
    folder = Path.cwd() / 'test_folder'
    elements = os.listdir(folder)
    count = 0
    n = 0
    for _ in elements:
        count += 1
    formatted_numbers = [str(i).zfill(num_digits) for i in range(1, 10 ** num_digits)]
    for element in elements:
        if element.endswith(source_ext):
            new_name = desired_name + formatted_numbers[n] + '.' + target_ext
            new_path = folder / new_name
            n += 1
            if not new_path.exists():  # Check if the new file name already exists
                (folder / element).rename(new_path)


# Решение 2
# def rename_files(desired_name, num_digits, source_ext, target_ext, name_range):
#     folder = Path.cwd() / 'test_folder'
#     files = folder.glob(f'*.{source_ext}')  # Получаем список файлов с указанным расширением
#     formatted_numbers = [str(i).zfill(num_digits) for i in range(1, len(files) + 1)]
#
#     for i, file in enumerate(files):
#         # Извлекаем часть имени файла в соответствии с указанным диапазоном
#         original_name_part = file.stem[name_range[0]:name_range[1]]
#         # Формируем новое имя файла
#         new_name = f"{desired_name}{original_name_part}{formatted_numbers[i]}.{target_ext}"
#         # Переименовываем файл
#         file.rename(folder / new_name)
#         print(f'Renamed {file.name} to {new_name}')


# Решение 3
# import os
#
# def rename_files(desired_name, num_digits, source_ext, target_ext, name_range=None):
#     new_names = []
#
#     # Получаем список файлов в текущей директории
#     files = os.listdir('test_folder')
#
#     # Фильтруем только нужные файлы с указанным расширением
#     filtered_files = [file for file in files if file.endswith(source_ext)]
#
#     # Сортируем файлы по имени
#     filtered_files.sort()
#
#     # Задаем начальный номер для порядкового номера
#     num = 1
#
#     # Переименовываем файлы
#     for file in filtered_files:
#         # Получаем имя файла без расширения
#         name = os.path.splitext(file)[0]
#
#         # Если задан диапазон, обрезаем имя файла
#         if name_range:
#             name = name[name_range[0]-1:name_range[1]]
#
#         # Создаем новое имя с желаемым именем, порядковым номером и новым расширением
#         new_name = desired_name + str(num).zfill(num_digits) + '.' + target_ext
#
#         # Переименовываем файл
#         path_old = os.path.join(os.getcwd(), folder_name, file)
#         path_new = os.path.join(os.getcwd(), folder_name, new_name)
#         os.rename(path_old, path_new)
#
#         # Увеличиваем порядковый номер
#         num += 1


# rename_files(desired_name="new_file_", num_digits=3, source_ext="doc", target_ext="txt")
# rename_files(desired_name="file_", num_digits=4, source_ext="txt", target_ext="txt")
rename_files(desired_name="new_file_", num_digits=1, source_ext="txt", target_ext="doc")

folder_content = ""
files = os.listdir(Path.cwd() / 'test_folder')
files.sort()
separator = ", "
files_as_string = separator.join(files)
print(files_as_string)
