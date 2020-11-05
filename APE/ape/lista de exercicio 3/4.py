nome = input('Nome: ').title()
sexo = input('Sexo (M/F): ').upper()
if sexo == 'M':
    print(f'Olá, senhor {nome}')
else:
    print(f'Olá, senhora {nome}')
