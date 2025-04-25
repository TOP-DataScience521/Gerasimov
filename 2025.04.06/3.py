def countable_nouns(num: int, yer: tuple[str, str, str]):

    # первая проверка на 1 - 9
    if num == 1: 
        return yer[0] 
    elif num in (2, 3, 4): 
        return yer[1]
    elif num in (0, 5, 6, 7, 8, 9):
        return yer[2]
    # проверка исключений  10 - 19
    elif 9 < num < 20:
        return yer[2]
    # проверка для 20 + без исключений
    elif num >= 20:
        num = str(num)
        if num[-1] == '1': 
            return yer[0]
        elif num[-1] in {'2', '3', '4'}: 
            return yer[1]
        elif num[-1] in {'0', '5', '6', '7', '8', '9'}:  
            return yer[2]


# >>> countable_nouns(365, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(9, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(11, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(20, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(33, ("год", "года", "лет"))
# 'года'
# >>>