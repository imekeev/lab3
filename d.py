def filter_prime(a):
    primes = []
    for x in a:
        p = True
        if x == 1:
            p = False
        for i in range(2, x):
            if x % i == 0:
                p = False
                break
        if p == True:
            primes.append(x)

    return primes

print(filter_prime([1, 2, 3, 4, 5, 17, 20, 109, 101]))
