import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("Координаты:", self.x, self.y)

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return int(math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2))  

x1 = int(input("Введите x для первой точки: "))
y1 = int(input("Введите y для первой точки: "))

x2 = int(input("Введите x для второй точки: "))
y2 = int(input("Введите y для второй точки: "))

# Создаём объекты точек
p1 = Point(x1, y1)
p2 = Point(x2, y2)

p1.show()
p2.show()

print("Расстояние между точками:", p1.dist(p2))
