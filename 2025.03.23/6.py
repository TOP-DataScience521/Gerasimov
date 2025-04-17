ticket = input('А твой билет счастливый?: ')


sum_st = 0
sum_fin = 0


for i in range(3):
    sum_st += int(ticket[i])
      
for i in range(3, 6):
    sum_fin += int(ticket[i])
    
    
if sum_st == sum_fin:
    print('да')
else:
    print('нет') 



# А твой билет счастливый?: 123321
# да