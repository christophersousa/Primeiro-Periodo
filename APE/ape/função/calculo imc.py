
#calculo do imc recebedo o peso e altura do usuario#
def calculo_imc(peso,alt):
    imc = peso/ (alt**2)
    return round(imc,2)

#Grau de Obesidade#
def grau(imc):
    if imc < 26:
        grau_ob = 'Normal'
    elif imc <= 26 and imc > 30:
        grau_ob = 'Obeso'
    else:
        grau_ob = 'Obeso Mórbido'
    return grau_ob


print('*'*26)
print('Vamos calcular o seu IMC ?')
print('*'*26)

#Usei o while para não precisar fazer todos os  30, fica opcional para o usuario#


while True:

    nome = input('\nNome: ').title()
    sexo = input('Sexo: ').lower()
    peso = int(input('Digite seu peso: '))
    alt = float(input('Digite sua altura: '))

    if sexo == 'feminino' or sexo == 'f' or sexo == 'mulher':
        sexo_user = 'Senhora'
    else:
        sexo_user = 'Senhor'
    
    imc = calculo_imc(peso, alt)
    grau_ob = grau(imc)

    print()
    print('-'*40)
    print('\nOlá,',sexo_user,nome,'!!')
    print(f'Seu calculo do imc é {imc}.')
    print(f'O seu grau de obesidade é {grau_ob}.')
    print()
    print('-'*40)
    
    cont = input('\nDeseja continuar ? ').upper()

    if cont == 'NÃO' or cont == 'N':
        break

print('Fim do programa!!')
