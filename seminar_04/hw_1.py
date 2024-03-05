# Напишите функцию для транспонирования матрицы transposed_matrix,
# принимает в аргументы matrix, и возвращает транспонированную матрицу.

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]


# Введите ваше решение ниже


def transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


# def transpose(matrix):
#     new_matrix = []
#     for i in range(len(matrix[0])):
#         new_row = []
#         for row in matrix:
#             new_row.append(row[i])
#         new_matrix.append(new_row)
#     return new_matrix


transposed_matrix = transpose(matrix)
print(transposed_matrix)


# Решение
# def transpose(matrix):
#     # определяем количество строк и столбцов в матрице
#     rows = len(matrix)
#     cols = len(matrix[0])
#
#     # создаем новую матрицу с размерами, поменянными местами
#     transposed = [[0 for row in range(rows)] for col in range(cols)]
#
#     # заполняем новую матрицу значениями из старой матрицы
#     for row in range(rows):
#         for col in range(cols):
#             transposed[col][row] = matrix[row][col]
#
#     return transposed