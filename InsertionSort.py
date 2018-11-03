

n= [3,9,6,7,8]

for c in range(0,len(n),+1):
    for z in range(c,0,-1):
        if n[z] > n[c]:
            print("if,pass")
            n[-1],n[z] = n[z],n[-1]


print(n)
