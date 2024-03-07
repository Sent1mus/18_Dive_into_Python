# Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
file_path = "C:/Users/User/Documents/example.txt"


# Введите ваше решение ниже

def get_file_info(file_path):
    # Разделение пути на путь и имя файла
    path, file_name_with_ext = file_path.rsplit('/', 1) if '/' in file_path else ('', file_path)
    # Добавление слеша в конец пути, если он отсутствует и не в текущем каталоге
    if not path.endswith('/') and path:
        path += '/'
    # Разделение имени файла на имя и расширение
    file_name, file_ext = file_name_with_ext.rsplit('.', 1) if '.' in file_name_with_ext else (file_name_with_ext, '')
    # Добавление точки к расширению файла
    file_ext = '.' + file_ext if file_ext else ''
    return path, file_name, file_ext


print(get_file_info(file_path))


# Решение

# def get_file_info(file_path):
#     file_name = file_path.split("/")[-1]
#     file_extension = file_name.split(".")[-1]
#     path = file_path[:-len(file_name)]
#     return (path, file_name[:-len(file_extension)-1], "." + file_extension)
