def unique_elements(lst):
    unique_list = []  
    for item in lst:
        if item not in unique_list:  # Если элемента ещё нет в списке, добавляем его
            unique_list.append(item)
    return unique_list

numbers = list(map(int, input("Введите числа через пробел: ").split()))

print(*unique_elements(numbers))
