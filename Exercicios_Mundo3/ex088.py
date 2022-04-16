aluno = dict()

aluno['Nome'] = str(input('Nome do Aluno: '))
aluno['Média'] = float(input('Média do Aluno: '))

print('==' * 30)

if aluno['Média'] <= 5:
    print(f'O aluno: {aluno["Nome"]}.')
    print(f'Possui a media: {aluno["Média"]:.1f}!')
    print(f'Sua situação é: REPROVADO!')

elif aluno['Média'] < 7:
    print(f'O aluno: {aluno["Nome"]}.')
    print(f'Possui a media: {aluno["Média"]:.1f}!')
    print(f'Sua situação é: RECUPERAÇÃO!')

elif aluno['Média'] >= 7:
    print(f'O aluno: {aluno["Nome"]}.')
    print(f'Possui a media: {aluno["Média"]:.1f}!')
    print(f'Sua situação é: APROVADO!')

