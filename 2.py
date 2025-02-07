class Shape:
    def area(self):
        print(0)

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        print(self.length ** 2)

x = Square(20)
x.area()

y = Square(500)
y.area()