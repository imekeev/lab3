def rev(s):
    s = s.split()
    s = s[::-1]
    return " ".join(s)

print(rev("i have a book"))