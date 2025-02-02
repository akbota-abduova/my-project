import math

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3 
r = float(input("radius: "))

# Вывод результата
print("volume:", sphere_volume(r))
