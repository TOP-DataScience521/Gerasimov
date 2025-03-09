import datetime


name = input('Введите имя: ')
surname = input('Введите фамилию: ')
year = input('Введите год рождения: ')


act_year = datetime.datetime.now().year


n_year = (act_year) - int(year)


print((name),' ' ,(surname),',' ,' ' ,(n_year), sep='')


#C:\Users\gera\Desktop>python 1.py
#Введите имя: Максим
#Введите фамилию: Герасимов
#Введите год рождения: 2001
#Максим Герасимов, 24