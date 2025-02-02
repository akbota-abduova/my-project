def solve(numheads, numlegs):
    for chickens in range(numheads + 1):  # Перебираем возможное количество кур
        rabbits = numheads - chickens  # Остаток — это кролики
        if (chickens * 2 + rabbits * 4) == numlegs:  
            return chickens, rabbits  
numheads = 35
numlegs = 94

chickens, rabbits = solve(numheads, numlegs)
print("Chikens:", chickens)
print("Rabbits:", rabbits)
