def histogram():
    numbers = list(map(int, input("Введите числа через пробел: ").split())) 
    for num in numbers:
        print("*" * num) 
histogram()
