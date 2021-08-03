doacao = 0
total = 0
reais = 0

while doacao != -1:
    doacao = float(input())
    if doacao != -1:
        total += doacao
    else:
        print(f'VC$ {total:.2f}')
        reais = (total * 2.5)
        print(f'R$ {reais:.2f}')