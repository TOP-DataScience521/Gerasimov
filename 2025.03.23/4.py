n = int(input('количество простых числе среди n значных: '))


start = int('1' + '0' * (n - 1))
fin = int('9' + '9' * (n - 1))
step = start
summ = 0

 
while step <= fin:
    if step < 2:
        step += 1
        continue
   


    for i in range(2, int(step ** 0.5) + 1):
        if step % i == 0:  
            break
    else:
        summ += 1
   
    step += 1  

print(summ)



# количество простых числе среди: 1
# 4

# количество простых числе среди: 3
# 143