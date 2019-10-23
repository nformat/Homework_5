class Room():

    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b


    def square(self):
        return self.a*self.b


    def perimeter(self):
        return (self.a+self.b)*2


    def __str__(self):
        return f"\nObject {self.__class__}\na= {self.a} , b= {self.b}"

s = Room(5, 10)
print("Площадь комнаты:", s.square())
print("Периметр комнаты:", s.perimeter())
print(s)

class Dot():

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


    def dist_zero(self):
        return ((self.x**2 + self.y**2) ** 0.5)


    def dist_to(self,b):
        return (((self.x - b.x) ** 2 + (self.y - b.y) ** 2) ** 0.5)

    def __str__(self):
        return f"\nObject {self.__class__}\na= {self.x} , b= {self.y}"


d = Dot(2, 2)
d2 = Dot(3, 3)
print("\nРасстояние от начала координат до точки: ", d.dist_zero())
print("Расстояние между двумя точками:", d.dist_to(d2))
print(d)
