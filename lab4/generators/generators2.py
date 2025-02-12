def even_numbers(n):
    even_nums = []
    for i in range(0, n+1, 2):
        even_nums.append(i)
    return even_nums

n = int(input("Enter a number n: "))

even_nums = even_numbers(n)

# Печатаем четные числа разделенные запятой
print(', '.join(map(str, even_nums)))
