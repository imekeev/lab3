def unique(a):
    b = []
    for x in a:
        if x not in b:
            b.append(x)
    return b

print(unique([1, 2, 1, 2, 4, 3, 3, 9]))