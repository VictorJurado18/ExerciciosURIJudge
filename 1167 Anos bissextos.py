ano_inicio = int(input())
ano_fim = int(input())
bissextos = 0
while ano_inicio <= ano_fim:
    if (ano_inicio %4 == 0 and ano_inicio % 100 != 0) or (ano_inicio % 400 == 0):
        print(ano_inicio)
        ano_inicio += 4
        bissextos += 1
    else:
        ano_inicio += 1
print(f'bissextos: {bissextos}')
