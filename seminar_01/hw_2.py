# #Напишите код, который анализирует число num и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если это число натуральное
# и делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
# Если подается отрицательное число или число более ста тысяч,
# выведите на экран сообщение: "Число должно быть больше 1 и меньше 100000".
# Внимание! Число 1 — не является ни простым, ни составным числом, так как у него только один делитель — 1.


# Мое решение ниже


num = 6
count = 0
if num <= 1 or num >= 100001:
    print("Число должно быть больше 1 и меньше 100000")
else:
    for i in range(2, num + 1):
        if num % i == 0:
            count += 1
    if count > 1:
        print("Не является простым")
    else:
        print("Простое")


# Эталонное решение ниже


# if not 1 < num <= 100000:
#     print("Число должно быть больше 1 и меньше 100000")
# else:
#     is_prime = True
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             print("Не является простым")
#             break
#     else:
#         print("Простое")