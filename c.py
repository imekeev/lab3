def solve(numheads, numlegs):
    y = numlegs//2 - numheads
    x = numheads - y
    return x, y

print(solve(35, 94))
