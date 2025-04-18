scores_letters = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}


word = input('Сыграем в "Эрудита"?: ').upper().replace('Ё', 'Е')

points = 0


for letter in word:  
    for n, letters in scores_letters.items():  
        if letter in letters:
            points += n
            break  


print(points)


# Сыграем в "Эрудита"?: синхрофазотрон
# 29

# Сыграем в "Эрудита"?: ёж
# 6