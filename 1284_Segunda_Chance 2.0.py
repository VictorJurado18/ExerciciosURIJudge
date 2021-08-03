alunos = int(input())
cont = 0
nts_originais = []
nts_bonus = []
simb = ''


def recebe_notas(notas,alunos):
    cont =0
    while cont != alunos:
        notas = float(input())
        nts_originais.append(notas)
        cont += 1
    return alunos


