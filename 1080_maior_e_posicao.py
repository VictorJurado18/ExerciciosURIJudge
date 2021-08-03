#Entrada
#O arquivo de entrada contém 100 números inteiros, positivos e distintos.

#Saída
#Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.

n = int(input())
res = 0
for i in range (1,100):
    a = int(input())
    if a > res:
        mai = a
        pos = i + 1
        res = a

print(mai)
print(pos)
