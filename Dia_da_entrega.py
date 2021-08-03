
dias_da_semana = ['domingo','segunda','terca','quarta','quinta','sexta','sabado']

dia_do_pedido = input()

prazo_de_chegada = int(input())

if prazo_de_chegada == 0:
    print("chega hoje!")
    quit()

numero = 0
parar = 0

while parar == 0:
    identifica_na_tabela = dias_da_semana[numero]
    if identifica_na_tabela == dia_do_pedido:
        parar = 1
    else:
        numero = numero + 1

contagem = 0

while contagem != prazo_de_chegada:
    if numero != 6:
        contagem = contagem + 1
        numero = numero + 1
    else:
        contagem = contagem + 1
        numero = 0

print('sera entregue {}'.format(dias_da_semana[numero]))