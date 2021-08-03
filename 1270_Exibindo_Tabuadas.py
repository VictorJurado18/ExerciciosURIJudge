a = int (input ())
b = int (input ())
lista = []
mult = 1
cont = 0
cont_lista = 0
if a > b:
    print('Nenhuma tabuada no intervalo!')
    quit()

for i in range (a, b + 1):
    lista.append (i)

while cont_lista != len(lista):
    while mult != 11:
        print(f'{lista[cont]} X {mult} =', lista[cont] * mult)
        mult += 1
    print('----------')
    cont_lista += 1
    cont += 1
    mult = 1
