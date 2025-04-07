yer = int(input('ваш год: '))

if yer % 4 == 0 and yer / 100 > 0 or yer % 400 == 0:
    print('да')
else:
    print('нет') 


# ваш год: 1941
# нет


# ваш год: 1940
# да

