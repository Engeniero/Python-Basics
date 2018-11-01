
def PerfectRoot_Checker(n):
    f = False
    for x in range(n):
        if x*x == n:
            f = True
    return  f

root = PerfectRoot_Checker(49)
print(root)
