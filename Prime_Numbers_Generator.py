x = int(input("Enter how much prime number you want: "))
y = 2
n = 0
for a in range(2,x,+1):
    y = 2
    f = True
    while a > y:
        if a % y == 0:
            f = False
            y = a
        y +=1
    if f == True:
        print(a)
        y +=1
        n +=1
print("\nPrime Numbers Generated",n)
