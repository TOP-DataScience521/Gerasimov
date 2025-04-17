from decimal import Decimal


n = input('Стоимость отправки 30 коп. за символ: ')


price = 0.30


n = len(n.replace(" ", ""))
msg = n * price
msg = Decimal(msg)


print(f"{msg // 1} руб. {int(msg % 1 * 100)} коп.")



# Стоимость отправки 30 коп. за символ: это сообщение стоит 8 руб. 40 коп.
# 8 руб. 40 коп.