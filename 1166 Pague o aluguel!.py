
#ENTRADA
#Dois números inteiros positivos, o primeiro
# representa o valor total da dívida e o segundo o valor que Ramón poderá pagar mensalmente.

#SAIDA
#O número do pagamento, o valor restante da dívida antes do pagamento
# mensal e o valor restante da dívida após o pagamento mensal, conforme o padrão exibido
# nos exemplos. A exibição deve continuar até que a dívida seja quitada.

#EXEMPLO
#pagamento: 1
#antes = 300
#depois = 250
#-----


d = int(input())
pm= int(input())
pg= 1

while d != 0:
    print(f"pagamento: {pg}")
    print(f"antes = {d}")
    d = d - pm
    if d < 0:
        d = 0
    print(f'depois = {d}')
    print('-----')
    pg += 1

