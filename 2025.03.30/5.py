cell_1 = input('Король стоит: ')
cell_2 = input('Король идет: ')



playing_field = {
    '1a': 1, '1b': 2, '1c': 3, '1d': 4, '1e': 5, '1f': 6, '1g': 7, '1h': 8,
    '2a': 1, '2b': 2, '2c': 3, '2d': 4, '2e': 5, '2f': 6, '2g': 7, '2h': 8,
    '3a': 1, '3b': 2, '3c': 3, '3d': 4, '3e': 5, '3f': 6, '3g': 7, '3h': 8,
    '4a': 1, '4b': 2, '4c': 3, '4d': 4, '4e': 5, '4f': 6, '4g': 7, '4h': 8,
    '5a': 1, '5b': 2, '5c': 3, '5d': 4, '5e': 5, '5f': 6, '5g': 7, '5h': 8,
    '6a': 1, '6b': 2, '6c': 3, '6d': 4, '6e': 5, '6f': 6, '6g': 7, '6h': 8,
    '7a': 1, '7b': 2, '7c': 3, '7d': 4, '7e': 5, '7f': 6, '7g': 7, '7h': 8,
    '8a': 1, '8b': 2, '8c': 3, '8d': 4, '8e': 5, '8f': 6, '8g': 7, '8h': 8
}


number_1  = int(cell_1[0])  #4b

number_2 = int(cell_2[0])  #3abc 4a_c 5abc

key_1 = playing_field[cell_1]

key_2 = playing_field[cell_2]


if number_1 == number_2 or number_1 == number_2 + 1 or number_1 == number_2 - 1:
    if key_1 == key_2 or key_1 == key_2 + 1 or key_1 == key_2 - 1:
        print('да') 
    else:
        print('нет')


else:
    print('нет')
    
    

# Король стоит: 2a
# Король идет: 1h
# нет

# Король стоит: 1a
# Король идет: 1h
# нет

# Король стоит: 4b
# Король идет: 3a
# да