id = 0
inp = 0
cont = 0
while inp >= 0 :
    inp = int(input())
    if inp >= 0:
        id += inp
        cont += 1
med_id = id /cont
print(f'{med_id:.2f}')