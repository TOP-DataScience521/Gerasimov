from decimal import Decimal


nm_1 = input('число 1: ')
nm_2 = input('число 2: ')
nm_3 = input('число 3: ')

nm_1 = Decimal(nm_1)
nm_2 = Decimal(nm_2)
nm_3 = Decimal(nm_3)

# ИСПРАВИТЬ: избыточное количество ветвлений
# ИСПРАВИТЬ: избыточное количество операций
if nm_1 > 0:
    num_1 = nm_1 + 0
elif nm_1 <= 0:
    num_1 = 0
    
if nm_2 > 0:
    num_2 = num_1 + nm_2
elif nm_2 <= 0:
    num_2 = num_1 + 0
    
if nm_3 > 0:
    num_3 = num_2 + nm_3
elif nm_3 <= 0:
    num_3 = num_2 + 0

print('сумма положительных чисел', num_3)


# число 1: 4
# число 2: -4
# число 3: 1.5
# сумма положительных чисел 5.5


# ИТОГ: 2/3

