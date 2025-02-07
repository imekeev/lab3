from itertools import permutations

def permut(s):
    ans = []
    p = permutations(s)
    for x in p:
        ans.append("".join(x))
    return ans

print(permut("book"))
