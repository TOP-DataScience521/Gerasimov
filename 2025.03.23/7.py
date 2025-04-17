n = int(input('последовательность Фибоначчи: '))


fibuch = [1, 1] 


if n == 0:
    print()  
elif n == 1:
    print(1)
elif n == 2:
    print(1, 1)
else:
    for i in range(2, n):
        next = fibuch[i-1] + fibuch[i-2]
        fibuch.append(next)
   

print(*fibuch)


# последовательность Фибоначчи: 17
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597