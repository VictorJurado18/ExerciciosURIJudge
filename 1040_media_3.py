notas = input().split()
n1,n2,n3,n4 = notas
media = (float(n1) * 2 + float(n2) * 3 + float(n3) * 4 + float(n4) * 1) / 10
print ('Media: {:.1f}'.format (media))
if media >= 7.0:
    print('Aluno aprovado.')

if media < 5:
    print('Aluno reprovado.')

if 5.0 <= media <= 6.9:
    print('Aluno em exame.')
    exame = float(input())
    print('Nota do exame: {}'.format(exame))
    media_final = (exame + media)/2
    if media_final >= 5:
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(media_final))
    else:
        print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(media_final))
