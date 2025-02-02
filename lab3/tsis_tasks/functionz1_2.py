def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

fahrenheit = float(input("Фаренгейт: "))
print("Цельсия:", fahrenheit_to_celsius(fahrenheit))
