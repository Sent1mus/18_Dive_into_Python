# На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
# Напишите программу, которая должна возвращать сумму и произведение дробей. Дроби упрощать не нужно.
# Для проверки своего кода используйте модуль fractions.


frac1 = "1/7"
frac2 = "3/4"
# Введите ваше решение ниже

import fractions
numerator1 = int(frac1[0])
denominator1 = int(frac1.partition('/')[2])
numerator2 = int(frac2[0])
denominator2 = int(frac2.partition('/')[2])

sum_numerator1 = numerator1 * denominator2
sum_numerator2 = numerator2 * denominator1
print(f"Сумма дробей: {(sum_numerator1 + sum_numerator2)}/{denominator1 * denominator2}")
print(f"Произведение дробей: {numerator1*numerator2}/{denominator1 * denominator2}")

print(f"Сумма дробей: {fractions.Fraction(frac1) + fractions.Fraction(frac2)}")
print(f"Произведение дробей: {fractions.Fraction(frac1) * fractions.Fraction(frac2)}")


# from fractions import Fraction
# #frac1 = '2/5'
# #frac2 = '3/5'
#
# # Разбиваем строки на числитель и знаменатель без использования map
# numerator1_str, denominator1_str = frac1.split('/')
# numerator2_str, denominator2_str = frac2.split('/')
#
# # Преобразуем строки в целые числа
# numerator1 = int(numerator1_str)
# denominator1 = int(denominator1_str)
# numerator2 = int(numerator2_str)
# denominator2 = int(denominator2_str)
#
# common_denominator = denominator1 * denominator2
#
# new_numerator1 = numerator1 * denominator2
# new_numerator2 = numerator2 * denominator1
#
# summation_numerator = new_numerator1 + new_numerator2
# multiplication_numerator = numerator1 * numerator2
#
# print(f"Сумма дробей: {summation_numerator}/{common_denominator}")
# print(f"Произведение дробей: {multiplication_numerator}/{common_denominator}")
#
# # Преобразуем введенные строки в объекты Fraction
# fraction1 = Fraction(frac1)
# fraction2 = Fraction(frac2)
#
# # Вычисляем сумму и произведение дробей
# summation = fraction1 + fraction2
# multiplication = fraction1 * fraction2
#
# print(f"Сумма дробей: {summation}")
# print(f"Произведение дробей: {multiplication}")
