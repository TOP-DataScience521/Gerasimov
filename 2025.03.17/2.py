nm_1 = int(input('число 1: '))
nm_2 = int(input('число 2: '))


if nm_1 % nm_2 == 0:
    num_1 = nm_1 / nm_2
    num_1 = int(num_1)
    print(f'{nm_1} делится на {nm_2} нацело\nчастное: {num_1}')
    
else:
    num_2 = nm_1 // nm_2
    num_3 = nm_1 % nm_2
    
    print(f'{nm_1} не делится на {nm_2} нацело\nнеполное частное: {num_2}\nостаток: {num_3}')
    
    
#C:\Users\gera\Desktop>python 2.py
#число 1: 20
#число 2: 5
#20 делится на 5 нацело
#частное: 4

#C:\Users\gera\Desktop>python 2.py
#число 1: 15
#число 2: 4
#15 не делится на 4 нацело
#неполное частное: 3
#остаток: 3