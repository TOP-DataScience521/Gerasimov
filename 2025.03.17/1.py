from decimal import Decimal


nm_1 = input('число 1: ')
nm_2 = input('число 2: ')
nm_3 = input('число 3: ')

nm_1 = Decimal(nm_1)
nm_2 = Decimal(nm_2)
nm_3 = Decimal(nm_3)

num = 0

if nm_1 > 0:
    num += nm_1
if nm_2 > 0:
    num += nm_2   
if nm_3 > 0:
    num += nm_3


print('сумма положительных чисел', num)


# число 1: 4
# число 2: -4
# число 3: 1.5
# сумма положительных чисел 5.5



