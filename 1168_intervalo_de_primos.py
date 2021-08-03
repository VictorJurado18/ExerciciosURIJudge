a = int(input())
b = int(input())
lista = []
if a == 1 or a == 0:
    a += 1
for l in range(a,b + 1):
    cont=0
    for p in range (1,l+1):
        if l % p == 0:
            cont += 1
    if cont <=2:
        lista.append(l)
        print(l)
print('primos: ', len(lista))

