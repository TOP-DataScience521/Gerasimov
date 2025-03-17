try:
    number = int(input('это однозначное число степень двойки?: '))

except ValueError:
    print('не является однозначным числом')

else: 
    
    if number <= -10 or number >= 10:
        print('не является однозначным числом')
        
    elif number <= 0:
        print('нет')
        
    elif number == 8 or number == 4 or number == 2 or number == 1:
        print ('да')
        
    else:
        print ('нет')
    
    
#C:\Users\gera\Desktop>python 4.py
#это однозначное число степень двойки?: -4
#нет
#
#C:\Users\gera\Desktop>python 4.py
#это однозначное число степень двойки?: 2
#да
#
#C:\Users\gera\Desktop>python 4.py
#это однозначное число степень двойки?: -4
#нет
#
#C:\Users\gera\Desktop>python 4.py
#это однозначное число степень двойки?: -11
#не является однозначным числом
#
#C:\Users\gera\Desktop>python 4.py
#это однозначное число степень двойки?: авава
#не является однозначным числом