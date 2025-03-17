yer = int(input('ваш год: '))


if yer % 4 == 0 and yer / 100 > 0 or yer % 400 == 0:
    print('да')
    
else:
    print('нет') 
    
    
#C:\Users\gera\Desktop>python 3.py
#ваш год: 1941
#нет

#C:\Users\gera\Desktop>python 3.py
#ваш год: 1940
#да