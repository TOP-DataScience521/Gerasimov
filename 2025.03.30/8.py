st = input('Введите двоичное число: ')


n = {'0', '1'}


if st.startswith('b'):
    detect = st[1:]
elif st.startswith('0b'):
    detect = st[2:]
else:
    detect = st
    

if set(detect) <= n:
    print('да')
else: 
    print('нет')


# Введите двоичное число: 101010
# да

# Введите двоичное число: b010
# да

# Введите двоичное число: 0b10101
# да

# Введите двоичное число: 010101b0101
# нет