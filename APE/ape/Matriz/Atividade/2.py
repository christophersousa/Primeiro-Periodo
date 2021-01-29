import random
nlin = int(input('Números de Alunos : '))
ncol = 5

cont_Media = 0
cont_Aluno = 0

a = [[None]*ncol for i in range(nlin)]

for i in range(nlin):
    
    print(f'\nAluno {i+1}°:')
    somador = 0
    for j in range(1,ncol -1):
        
       a[i][j] = random.randint(1,10)
       somador += a[i][j]
       
    print()
    
    a[i][0] = input('Nome do aluno: ')
    
    media = somador/ (ncol - 1)
    a[i][4]= media
    cont_Media += media
    
    if media >= 7:
        cont_Aluno += 1
        

print(f'-'*35)
print('  Nota 1°  Nota 2°  nota 3°  Média')

for i in range(nlin):
    for j in range(ncol):
        if j == 0:
            print({a[i][0]}, end = ' ')
            
        print(f'{a[i][j]:8.2f}', end = '')
    print()
print(f'-'*35)
Media_geral = cont_Media / nlin

print(f'\nA media geral da turmar é: {Media_geral:.2f}')
print(f'Números de alunos aprovados: {cont_Aluno}')
