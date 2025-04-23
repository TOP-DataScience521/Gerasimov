n_1 = input('Ввод_1: ').replace(" ", "")
n_2 = input('Ввод_2: ').replace(" ", "")


nl_1 = len(n_1)
nl_2 = len(n_2)


if nl_2 == 0:
    print('да')
elif nl_1 < nl_2: 
    print('нет')
else:
    if n_2 in n_1:
        print('да')
    else:
        print('нет')


# Ввод_1: 1 2 3 4 5 6
# Ввод_2: 1 2 3
# да

# Ввод_1: 1 2 3 4 5 6
# Ввод_2: 2 4 5
# нет