# Дан список повторяющихся элементов lst. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
lst = [1, 1, 1, 1, 1]


# Введите ваше решение ниже


# def duplicates(my_list) -> list:
#     # Список из дублируемых значение, сложность n^2
#     new_list = []
#     for item in my_list:
#         if my_list.count(item) > 1:
#             if item not in new_list:
#                 new_list.append(item)
#     return new_list

def duplicates(my_list) -> list:
    # Линейная сложность O(n)
    count_dict = {}
    for item in my_list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return [item for item, count in count_dict.items() if count > 1]


duplicate_lst = list(duplicates(lst))
print(duplicate_lst)
