n = int(input())
cont = 0
mult = 2
while cont != n:
    for p in range (2,n +1):
        if p % 2 == 0:
            print(f"{p}^{mult} = {p**2}")
            cont += 2