def spy_game(nums):
    code = [0, 0, 7]  # Шаблон который мы ищем
    for num in nums:
        if num == code[0]:  # Если найден первый элемент шаблона
            code.pop(0)  # Удаляем его из списка
        if not code:  # Если список code пустой, значит "007" найдено
            return True
    return False  

print(spy_game([1, 2, 4, 0, 0, 7, 5]))  
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  
