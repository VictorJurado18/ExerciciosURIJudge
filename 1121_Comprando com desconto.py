#Um número real positivo na primeira linha, indicando o preço da mercadoria,
# um número inteiro positivo na segunda linha, indicando a quantidade comprada da mercadoria.

preco_da_mercadoria = float(input())
quantidade_comprada = int(input())
preco_total = preco_da_mercadoria * quantidade_comprada
desconto_fixo = preco_total* 0.1
desconto_variavel = preco_total * (quantidade_comprada * 0.01)
preco_desconto = preco_total - desconto_variavel - desconto_fixo

print("{:.2f}".format(preco_total))
print("{:.2f}".format(preco_desconto))