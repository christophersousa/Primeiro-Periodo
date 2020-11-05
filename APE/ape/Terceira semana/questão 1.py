nome = input('Nome do paciente: ')
sexo = input('Sexo (M/F): ')
alt = float(input('Altura: '))
if (sexo == 'M' or 'm'):
    imc = (72.7*alt)-58.0
    print(nome)
    print(f'De acordo com o calculo IMC, o seu peso ideal é {imc:.2f}´')
else:
    imc = (62.1*alt)-44.7
    print(nome)
    print(f'De acordo com o calculo IMC, o seu peso ideal é {imc}')
    
