number_n = input('Введите желаемое 3-x значное число: ')


number_3 = int(number_n) // 100
number_2 = (int(number_n) - (number_3) * 100) // 10
number_1 = (int(number_n) - (number_3) * 100 - (number_2) * 10) // 1

summa = number_3 + number_2 + number_1
isumma = int(summa)

der = number_3 * number_2 * number_1
ider = int(der)


print(f"Сумма цифр = {isumma} {'\n'}Произведение цифр = {ider}")


#C:\Users\gera\Desktop>python 4.py
#Введите желаемое 3-x значное число: 202
#Сумма цифр = 4
#Произведение цифр = 0

#инетресная задача с подвохом