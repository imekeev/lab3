class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"x: {self.x}, y: {self.y}")
    
    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, point):
        x1 = self.x
        y1 = self.y
        x2 = point.x
        y2 = point.y
        print(((x2 - x1) ** 2 + (y2 - y1)** 2)**(1/2))

a = Point(5, 6)
b = Point(10, 20)
a.dist(b)