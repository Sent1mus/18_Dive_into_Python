# Создайте функцию generate_csv_file(file_name, rows),
# которая будет генерировать по три случайны числа в каждой строке,
# от 100-1000 строк, и записывать их в CSV-файл. Функция принимает два аргумента:
#
# file_name (строка) - имя файла, в который будут записаны данные.
# rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.
#
# Создайте функцию find_roots(a, b, c), которая будет находить корни квадратного уравнения
# вида ax^2 + bx + c = 0. Функция принимает три аргумента:
#
# a, b, c (целые числа) - коэффициенты квадратного уравнения.
#
# Функция возвращает:
# None, если уравнение не имеет корней (дискриминант отрицателен).
# Одно число, если уравнение имеет один корень (дискриминант равен нулю).
# Два числа (корни), если уравнение имеет два корня (дискриминант положителен).
#
# Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots.
# Декоратор выполняет следующие действия:
# Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].
# Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.
# Сохраняет результаты в формате JSON в файл results.json.
# Каждая запись JSON содержит параметры a, b, c и результаты вычислений.
# Таким образом, после выполнения функций generate_csv_file и find_roots в файле results.json будет сохранена информация
# о параметрах и результатах вычислений для каждой строки данных из CSV-файла.
import csv
import json
import random


def generate_csv_file(file_name, rows):
    minimum_rows = 100
    maximum_rows = 1000
    if minimum_rows <= rows <= maximum_rows:
        print('True')
        with open(file_name, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['a', 'b', 'c'])
            writer.writeheader()
            for _ in range(rows):
                my_dict = {'a': random.randint(1, 10), 'b': random.randint(1, 10), 'c': random.randint(1, 10)}
                writer.writerow(my_dict)
    else:
        print("Количество строк в файле не находится в диапазоне от 100 до 1000.")


# Вариант2
# def generate_csv_file(file_name, rows):
#     with open(file_name, 'w', newline='') as f:
#         writer = csv.writer(f)
#         for i in range(rows):
#             row = [random.randint(1, 1000) for _ in range(3)]
#             writer.writerow(row)

def save_to_json(func):
    def wrapper(*args):
        result_list = []
        with open(args[0], 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                a, b, c = map(int, row)
                result = func(a, b, c)
                data = {'parameters': [a, b, c], 'result': result}
                result_list.append(data)
        with open('results.json', 'w') as f:
            json.dump(result_list, f)
    return wrapper


@save_to_json
def find_roots(a,b,c):
    D = b ** 2 - 4 * a * c
    if D < 0:
        return None
    elif D == 0:
        return -b / (2 * a)
    else:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        return x1, x2


file_name = 'input_data.csv'
rows = 100

generate_csv_file(file_name, rows)
find_roots(file_name)
