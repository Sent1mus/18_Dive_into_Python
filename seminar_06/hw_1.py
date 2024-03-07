# Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем.
# На вход будет подаваться дата в формате "день.месяц.год".
# Ваша задача - создать программу, которая проверяет, является ли введенная дата корректной или нет.
#
# Ваша программа должна предоставить ответ "True" (дата корректна)
# или "False" (дата некорректна) в зависимости от результата проверки.

date_to_prove = '28.2.2021'


def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False


def func(arg: str) -> bool:
    day, month, year = map(int, arg.split("."))
    if 1 <= year <= 9999:
        if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
            return True
        elif month in [4, 6, 9, 11] and 1 <= day <= 30:
            return True
        elif month == 2:
             if 1 <= day <= 29 and is_leap_year(year):
                return True
             elif 1 <= day <= 28 and not is_leap_year(year):
                return True
        else:
            return False
    return False


print(func(date_to_prove))


# Решение
# from sys import argv
#
# def is_leap(year: int) :
#     return not (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0))
#
# def valid(full_date: str) :
#     date, month, year = (int(item) for item in full_date.split('.'))
#     if year < 1 or year > 9999 or month < 1 or month > 12 or date < 1 or date > 31:
#         return False
#     if month in (4, 6, 9, 11) and date > 30:
#         return False
#     if month == 2 and is_leap(year) and date > 29:
#         return False
#     if month == 2 and not is_leap(year) and date > 28:
#         return False
#     return True
#
# if len(argv) > 1:
#     print(valid(argv[1]))
# else:
#     print(valid(date_to_prove ))
