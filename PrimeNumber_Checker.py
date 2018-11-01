
def PrimeNumberChecker(n):
    y = 2
    f = True
    if n != 1:
        while n > y:
            if n % y == 0:
                f = False
                y = n
            y += 1
    else:
        f = False
    return f

Prime = PrimeNumberChecker(1)
print(Prime)
