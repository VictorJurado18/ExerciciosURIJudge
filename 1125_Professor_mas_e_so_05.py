#prova substitutiva só substitui a nota da prova
#media 6

nt = float(input())
nt = nt / 2
np = float(input())
np = np / 2

media = nt + np

if media >=6:
    print('aprovado')
else:
    if nt >= 1:
        print("talvez com a sub")
    else:
        print("reprovado")

