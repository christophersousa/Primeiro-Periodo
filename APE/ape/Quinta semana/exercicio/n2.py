stop = 0
print(f'Esse programa serve para calcular a idade dos visitantes de um show e dizer a media da idade e que idade é mais presente no show. \nPara encerrar o program digite {stop}')
num = int(input('\nDigite a idade do visitante do show: '))
maior = num
menor = num
i = 0
cont = 0
quant = 0
quant1 = 0
while num != stop:
    i = i +1
    cont = cont + num
    media = cont / i

    if num >= 18 and num <= 21:
        quant = quant + 1
    else:
        quant1 = quant1 + 1 

    if num > maior:
        maior = num

    if num < menor:
        menor = num

    num = int(input('\nDigite a idade do visitante do show: '))
    
    total = quant + quant1
    perc = (quant / total * 100)

print(f'\nA media da idade dos visitantes é {media}')
print(f'A pessoa mais velha a entrar no show tem {maior} idade.\nO mais jovem a entrar no show tem {menor} idade')
print(f'A porcentagem de pessoas entre 18 anos e 21 anos é de {perc}%')
