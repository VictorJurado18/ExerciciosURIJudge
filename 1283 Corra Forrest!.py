tempo = 1
lista = []
while tempo >0:
    tempo = int(input())
    if tempo >=0:
        lista.append(tempo)
media = sum(lista) / len(lista)
print(f'MEDIA: {media:.2f}')

for n in lista:
    if n < media:
        print(n)

