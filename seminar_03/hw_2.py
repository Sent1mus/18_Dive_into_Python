# В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
# Слова разделяются пробелами. Такие слова как don t, it s, didn t итд (после того, как убрали знак препинания апостроф) считать двумя словами.
# Цифры за слова не считаем.
# Отсортируйте по убыванию значения количества повторяющихся слов. Слова выведите в обратном алфавитном порядке.


text = 'Hello world. Hello Python. Hello again.'

# Введите ваше решение ниже

import re

def clean_text(text):
    # Удаляем все знаки препинания, апострофы и цифры, заменяя их на пробелы
    text = re.sub(r'[^\w\s]', ' ', text) # Удаляем знаки препинания и специальные символы
    text = re.sub(r'\d+', ' ', text) # Удаляем все цифры
    text = re.sub(r'\s+', ' ', text) # Убираем лишние пробелы
    words = text.lower().split()
    return words


def count_elements(my_text) -> dict:
    """
    Count unique elements in text
    :param my_text:
    :return:
    """
    element_counts = {}
    for element in my_text:
        if element in element_counts:
            element_counts[element] += 1
        else:
            element_counts[element] = 1
    return element_counts


clean_text_list = clean_text(text)
my_dict = count_elements(clean_text_list)

# Создаем сортированный список кортежей в обратном порядке максимум 10 используя срез
sorted_dict_items = sorted(my_dict.items(), key=lambda x: (x[1], x[0]), reverse=True)[:10]

print(sorted_dict_items)

# Решение
# import re
# from collections import Counter
#
# # Удаляем знаки препинания и приводим текст к нижнему регистру
# cleaned_text = ''.join(char.lower() if char.isalpha() or char.isspace() else ' ' for char in text)
#
# # Разбиваем текст на слова и считаем их количество
# words = cleaned_text.split()
# word_counts = {}
#
# for word in words:
#     if word not in word_counts:
#         word_counts[word] = 1
#     else:
#         word_counts[word] += 1
#
# # Получаем 10 самых часто встречающихся слов
# top_words = sorted(word_counts.items(), key=lambda x: (x[1], x[0]), reverse=True)[:10]
#
# print(top_words)
