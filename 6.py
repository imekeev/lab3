a = [1, 2, 5, 6, 120, 17, 15]

def check(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

x = filter(check, a)
print(list(x))



a = [1, 2, 5, 6, 120, 17, 15]
x = filter(lambda x: x != 1 and all(x % i != 0 for i in range(2, x)), a)
print(list(x))