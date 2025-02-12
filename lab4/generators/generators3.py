def divisible_by_3_and_4(n):
    result = []
    for i in range(0, n+1):
        if i % 3 == 0 and i % 4 == 0:
            result.append(i)
    return result

n = int(input("Enter a number n: "))

numbers = divisible_by_3_and_4(n)

for number in numbers:
    print(number)
