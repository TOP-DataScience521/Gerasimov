tuti_fruits = []


while True:
    fruits = input('Ваши фрукты: ')
    if fruits == '':
        break
    tuti_fruits.append(fruits)
        


if len(tuti_fruits) == 0:
    marmalade = ''
    
elif len(tuti_fruits) == 1:
    marmalade = f'{tuti_fruits[0]}'
    
elif len(tuti_fruits) == 2:
    marmalade = f'{tuti_fruits[0]} и {tuti_fruits[1]}'
    
else:
    marmalade = ', '.join(tuti_fruits[:-1]) + ' и ' + (tuti_fruits[-1])
    
    
print(f'Вам нужны мармиладки со вкусоми: {marmalade}')


# Ваши фрукты: яблоко
# Ваши фрукты:
# Вам нужны мармиладки со вкусоми: яблоко

# Ваши фрукты: яблоко
# Ваши фрукты: мандарин
# Ваши фрукты:
# Вам нужны мармиладки со вкусоми: яблоко  и мандарин

# Ваши фрукты: яблоко
# Ваши фрукты: мандарин
# Ваши фрукты: ананас
# Ваши фрукты:
# Вам нужны мармиладки со вкусоми: яблоко, мандарин и ананас