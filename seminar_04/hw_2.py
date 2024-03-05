# Напишите функцию key_params, принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

# Введите ваше решение ниже


def key_params(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if not isinstance(value, (int, float, str, bytes, bool, type(None))):
            value = str(value)
        result[value] = key
    return result


params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
print(params)



# # Решение
# def key_params(**kwargs):
#     result = {}
#     for key, value in kwargs.items():
#         if value is None:
#             result[value] = key
#         elif isinstance(value, (int, str, float, bool, tuple)):
#             result[value] = key
#         else:
#             result[str(value)] = key
#     return result



