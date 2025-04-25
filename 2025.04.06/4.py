    # Ключи словаря:
        # 'median' — медиана
        # 'arithmetic' — среднее арифметическое
        # 'geometric' — среднее геометрическое
        # 'harmonic' — среднее гармоническое




# импорт корня и преобразования в словарь
from typing import Dict
import statistics


def central_tendency(num1: float, num2: float, *numbers: float) -> Dict[str, float]:
    
    # объединяем  сортируем
    full = [num1, num2, *numbers]
    sort_num = sorted(full)
    # вычисляем n 
    n = len(sort_num)
    
    # медиана  3, 7, 1, 6, 9 => 1, 3, 6, 7, 9 медианная 6  /|\  1, 3, 7, 9 медианная (3+7)/2= 5
    # проверяем длинну списка если она не четная вычисления не нужны если четная вычисляем
    if n % 2 == 0:
        median = (sort_num[n // 2] + sort_num[n // 2 - 1]) / 2 
    else:
        median = sort_num[n // 2]
        
    # среднее арифметическое (a1 + b2 + ... + cn) / n
    arithmetic = sum(sort_num) / n
    
    # среднее геометрическое n * math.sqrt(a1 * b2 * ... * cn) корень
    geometric = statistics.geometric_mean(sort_num)
    
    # среднее гармоническое n / (1/a1 + 1/b2 + ... + 1/cn)
    harmonic = statistics.harmonic_mean(sort_num)


    final = {
        'median': median,
        'arithmetic': arithmetic,
        'geometric': geometric,
        'harmonic': harmonic
    }
    
    return print(final)


# >>> central_tendency(1, 2, 3, 4)
# {'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.2133638394006434, 'harmonic': 1.92}
# >>> sample = [1, 3, 2, 4]
# >>> central_tendency(*sample)
# {'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.2133638394006434, 'harmonic': 1.92}
# >>> sample = [1, 2, 3, 4, 5]
# >>> central_tendency(*sample)
# {'median': 3, 'arithmetic': 3.0, 'geometric': 2.6051710846973517, 'harmonic': 2.18978102189781}
# >>> central_tendency(1, 3, 2, 4, 5)
# {'median': 3, 'arithmetic': 3.0, 'geometric': 2.6051710846973517, 'harmonic': 2.18978102189781}
# >>>