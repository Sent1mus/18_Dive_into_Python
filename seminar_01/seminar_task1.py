low = 0
decimal_num = 10
three_digit = 100
high = 1000
result = None
while True:
    number = int(input("Enter number: "))
    if number < 1 or number > 999:
        print(("Wrong number"))
    else:
        break
if low < number < decimal_num:
    result = number ** 2
elif decimal_num <= number < three_digit:
    last_digit = number % 10
    first_digit = number // 10
    result = first_digit * last_digit
elif three_digit <= number < high:
    if number > 0:
        temp1 = number % 10 * 100
        temp2 = number // 10 % 10 * 10
        temp3 = number // 100
        print(temp1, temp2, temp3)
        result = temp1 + temp2 + temp3
print(result)
