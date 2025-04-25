
# c**2 = a**2 + b**2

  #    |\
  #    | \
  #   b|  \ c
  #    | 90\    
  #    |____\
  #       a        
import math

def orth_triangle(*, cathetus_1: float = None, cathetus_2: float = None, hypotenuse: float = None) -> float | None:
    # вычисляем катет 2
    if cathetus_2 == None:
        cathetus_2 = hypotenuse**2 - cathetus_1**2
        # проверяем нет ли отрицательных значений
        if cathetus_2 > 0:
            cathetus_2 = math.sqrt(cathetus_2)
            return cathetus_2
        else:
            return None
    # вычисляем гипотенузу
    elif hypotenuse == None:
        hypotenuse = cathetus_1**2 + cathetus_2**2
        hypotenuse = math.sqrt(hypotenuse)
        return hypotenuse
    # если не передали 1 значение
    elif cathetus_1 == None:
        return None
    else:
        return None


# >>> print(orth_triangle(cathetus_1=3, hypotenuse=2))
# None
# >>> print(orth_triangle(cathetus_2=9, hypotenuse=3))
# None
# >>> orth_triangle(cathetus_1=8, cathetus_2=15)
# 17.0
# >>> orth_triangle(cathetus_1=3, hypotenuse=5)
# 4.0