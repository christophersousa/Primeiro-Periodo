quant = 0
print(f'O programa termina quando a matricula for {quant}')

mat = int(input('\nMatricula do Aluno: '))

while mat != quant:
    nome = input('Nome do Aluno: ').title()
    n1 = float(input('1° Nota: '))
    n2 = float(input('2° Nota: '))
    

    media = (n1+ n2) / 2
    
    if media >= 7:
        result = 'Aprovado'
    else:
        result = 'reprovado'

    print(f'\nO Aluno {nome} \nDe matricula: {mat} \nNota 1°: {n1} \nNota 2°: {n2} \nMédia: {media: .1f} \nSituação: {result}')

    mat = int(input('\nMatricula do Aluno: '))

print('fim do programa')
