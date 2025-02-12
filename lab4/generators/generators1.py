def square_up_to(n):
    result = [] #пустой список
    for i in range(1, n+1):
        result.append(i ** 2) 
    return result

N = int(input("Enter a number N: "))

squares = square_up_to(N)
for square in squares:
    print(square)
