# Entrada...
# Um número natural maior ou igual a dois.

# Saida...
# Dois números naturais, separados por um espaço, em que o primeiro é o número ímpar
# que antecede o valor dado na entrada e o segundo é o par que sucede o valor dado na entrada.

N = int(input())
resto = N % 2

if resto == 0:
    print(N - 1, N + 2)
else:
    print(N - 2,N + 1)