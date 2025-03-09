mil= input('Введите целое число миль: ')
mill= input('Введите дрорбный остаток миль: ')


km = (int(mil) + int(mill) * 0.1) * 1.61
n_km = round (km, 1)


print(f"{mil}.{mill} миль = {n_km} км")


#C:\Users\gera\Desktop>python 5.py
#Введите целое число миль: 12
#Введите дрорбный остаток миль: 9
#12.9 миль = 20.8 км