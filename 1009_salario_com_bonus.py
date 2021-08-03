nome = input()
salario_f = float(input())
vendas_mes = float(input())
vendas_mes = vendas_mes * 0.15
total = salario_f + vendas_mes

print ("TOTAL = R$ {:.2f}".format(total))