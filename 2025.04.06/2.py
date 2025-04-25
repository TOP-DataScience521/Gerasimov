def taxi_cost(metr , time = 0) -> int | None:
    # невозможный вариант
    if metr < 0 or time < 0:
        return None
    # поездка до 150 м
    elif 0 < metr <= 150:
        price = 80 + (time * 3) 
        price = round(price, 0)
        return int(price)
    # поездка отменена    
    elif metr <= 0 and time > 0:
        price = 160 + (time * 3)
        price = round(price, 0)
        return int(price)
    # стоимость проезда
    elif metr > 150:
        price = 80 + metr * 0.04 + (time * 3) 
        price = round(price, 0)
        return int(price)


# >>> print(taxi_cost(-300))
# None
# >>> taxi_cost(15000, 9)
# 707
# >>> taxi_cost(0, 9)
# 187
# >>> taxi_cost(15000)
# 680
# >>>