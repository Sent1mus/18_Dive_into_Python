# Напишите программу, которая получает целое число num и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

num = 257

# Введите ваше решение ниже

temp = num
s = ""
while temp > 0:
    if temp % 16 < 10:
        s += (str(temp % 16))
        temp = temp // 16
    else:
        if temp % 16 == 10:
            s += "A"
            temp = temp // 16
        elif temp % 16 == 11:
            s += "B"
            temp = temp // 16
        elif temp % 16 == 12:
            s += "C"
            temp = temp // 16
        elif temp % 16 == 13:
            s += "D"
            temp = temp // 16
        elif temp % 16 == 14:
            s += "E"
            temp = temp // 16
        elif temp % 16 == 15:
            s += "F"
            temp = temp // 16
print(f"Шестнадцатеричное представление числа: {s[::-1]}")
print(f"Проверка результата: {hex(num)}")


# Эталонное решение

HEX = 16
hex_digits = "0123456789ABCDEF"

hex_num = ""
test_hex_num = hex(num)

while num > 0:
    remainder = num % HEX
    hex_num = hex_digits[remainder] + hex_num
    num //= HEX
    print(remainder, hex_num, num )

print("Шестнадцатеричное представление числа:", hex_num)
print("Проверка результата:", test_hex_num)


