import datetime


name = input('Введите имя: ')
surname = input('Введите фамилию: ')
year = input('Введите год рождения: ')

act_year = datetime.datetime.now().year
n_year = act_year - int(year)

print(name, ' ' , surname, ',' , ' ', n_year, sep='')


# Введите имя: Максим
# Введите фамилию: Герасимов
# Введите год рождения: 2001
# Максим Герасимов, 24


# ИТОГ: 2/2


# КОММЕНТАРИЙ: PEP 8 — сборник рекомендаций по стилистическому оформлению Python кода — их стоит использовать для большего удобства чтения своего и чужого кода: https://peps.python.org/pep-0008/

