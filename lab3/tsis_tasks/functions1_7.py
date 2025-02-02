def has_33(nums):
    for i in range(len(nums) - 1):  # Перебираем индексы списка до предпоследнего элемента
        if nums[i] == 3 and nums[i + 1] == 3:  # Проверяем пару чисел
            return True
    return False
numbers = list(map(int, input("Введите числа через пробел: ").split()))
print(has_33(numbers))
