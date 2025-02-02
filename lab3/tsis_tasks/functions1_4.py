def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Проверяем делители до √n
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return filter(is_prime, numbers)  # Используем filter() 

numbers = map(int, input().split())

print(*filter_prime(numbers))
