class A:
    def getString(self):
        self.s = input()
    def printString(self):
        print(self.s)

p = A()
p.getString()
p.printString()