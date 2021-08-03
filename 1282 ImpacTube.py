n = int(input())
recebe = 0
lista = []

while recebe != n:
    a,b,c,d = input().split(';')
    b = int(b)
    c = float(c)
    lista.append([a,b,c,d])

    recebe += 1
val1 = float(input())
val2 = float(input())

print('''-----
BÔNUS
-----''')
premium = 0
cont = 0

while cont != n:
    if lista[cont][3] == 'sim':
        premium = val1
    else:
        premium = val2
    calc = float((lista[cont][1]//1000)*premium+lista[cont][2])

    print(f'{lista[cont][0]}: R$ {calc:.2f}')
    cont += 1
