number_n = int(input('Введите желаемое 3-x значное число: '))


number_3 = number_n // 100 
number_2 = number_n // 10 % 10
number_1 = number_n % 10


print(f"Сумма цифр = {number_1 + number_2 + number_3} {'\n'}Произведение цифр = {number_1 * number_2 *number_3}")


# Введите желаемое 3-x значное число: 202
# Сумма цифр = 4
# Произведение цифр = 0


