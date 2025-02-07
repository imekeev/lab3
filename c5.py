class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, n):
        self.balance += n

    def withdraw(self, n):
        if n > self.balance:
            print("You are poor!!!")
        else:
            self.balance -= n
            print(f"You withdrawed {n} dollars")
    

a = Account("Akniyet", 10000)
a.deposit(5000)
a.withdraw(1000)
print(a.balance)