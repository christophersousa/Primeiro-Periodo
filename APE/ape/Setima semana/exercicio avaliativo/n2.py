
i = 0
media = 0
total_idade = 0

idade_maior = -100
idade_menor = 100
nome_maior = 'string'
nome_menor = 'string'

ingresso = 0

while True:
    nome = input('\nNome do cliente: ').title()
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ').upper()

    if idade < 0:
        print('\nDigite as informações corretamente')
        continue
    
    if sexo != 'M' and sexo != 'F':
        print('\nDigite as informações corretamente')
        continue  

    if  idade > idade_maior:
        idade_maior = idade
        nome_maior = nome
        
    if idade < idade_menor:
        idade_menor = idade
        nome_menor = nome


    if sexo == 'M':
        ingresso = ingresso + 20

    else:
        ingresso = ingresso + 10


    i = i + 1
    total_idade = total_idade + idade
    media = total_idade / i

    cont = input('\nDesja continuar? ').upper()

        if cont == 'FIM' or cont == 'NÃO' or cont == 'N':
            break

        if cont != 'SIM' and cont != 'CONTINUAR' and cont != 'S':
            print(f'\nDigite as informações corretamente')
            continue  
        
print(f'\n{nome_maior} é o cliente mais velho com {idade_maior} anos.')
print(f'{nome_menor} é o cliente mais novo com {idade_menor} anos.')
print(f'\nA média das idades de todos os clientes é {media: .2f}.')
print(f'Total do apurado na noite {ingresso: .2f}R$')
