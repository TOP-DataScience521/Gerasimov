file = input('Введите имена файлов разделяя их ";": ').replace(" ", "").split(';')
# 1.py; 1.py; src.tar.gz; aux.h; main.cpp; functions.h; main.cpp; 1.py; main.cpp; src.tar.gz


counter_file = {} # общее количество файлов
detect_counter = {} # номер копии
file_in_system = [] # результат


for name in file:
    detect_counter[name] = 0

# считает количества каждого имени файла
# если оно повторяеться счетчик растет 
for name in file:
    if name in counter_file:
        counter_file[name] += 1
    else:
        counter_file[name] = 1

# генерация новых имен
# перыфй файл без изменений 
# присваиваем копиям новый номер
for name in file:
    detect_counter[name] += 1
    num = detect_counter[name]
    if num == 1:
        new_name = name
    else:
        if '.' in name:
            base, ext = name.rsplit('.', 1)
            new_name = f'{base}_{num}.{ext}'
        else:
            new_name = f'{name}_{num}'
    file_in_system.append(new_name)
    
# печатаем и сорируем 
for name in sorted(file_in_system):
    print(name)
    
    
# 1.py
# 1_2.py
# 1_3.py
# aux.h
# functions.h
# main.cpp
# main_2.cpp
# main_3.cpp
# src.tar.gz
# src.tar_2.gz