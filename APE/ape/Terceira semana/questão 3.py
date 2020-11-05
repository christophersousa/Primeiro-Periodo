valor = float(input('digite o valor da compra: '))
if valor >= 100:
    calculo = valor - 20
    print('Seu desconto é de R$ 20,00')
    print(f'valor final = {calculo}')
elif valor >= 50:
    calculo = valor - 5
    print('Seu desconto é de R$ 5,00')
    print(f'valor final = {calculo}')
if valor < 50:
    calculo = valor
    print('não há desconto')
    print(f'valor final = {calculo}')

else:
    print('Obrigado e volte sempre.')
