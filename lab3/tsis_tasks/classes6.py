def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True  

user_input = input("Введите числа через пробел: ")

# Преобразуем ввод в список чисел
numbers = list(map(int, user_input.split()))

# Фильтруем только простые числа через lambda
prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Простые числа:", prime_numbers)
