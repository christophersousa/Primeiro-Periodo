inicio = input("Iniciar programa ?  ").upper()

conA = 0
conB = 0
conC = 0

while inicio != 'FIM':
    aluno = input('Nome do aluno: ').title()
    n1 = int(input('1° Nota: '))
    n2 = int(input('2° Nota: '))
    n3 = int(input('3° Nota: '))

    media = (n1 + n2 + n3) / 3

    if media >= 7:
        con= 'A'
        sit = 'Aprovado'
    elif media <7 and media >= 4:
        con = 'B'
        sit = 'na final'
    else:
        con = 'C'
        sit = 'reprovado'

    if con == 'A':
        conA = conA + 1
    elif con == 'B':
        conB = conB + 1
    else:
        conC = conC + 1

    print(f'\n{aluno}\nEstá {sit} com a média {media: .2f}.')

    inicio = input("\nDeseja continuar ( para encerrar digite fim) ?  ").upper()

print(f'foram categorizados no conceito A {conA} alunos(as)')
print(f'foram categorizados no conceito B {conB} alunos(as')
print(f'foram categorizados no conceito C {conC} alunos(as')

    
    
