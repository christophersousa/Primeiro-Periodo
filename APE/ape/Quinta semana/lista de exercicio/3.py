quant = 0
print(f' Digite alguns números para sabermos qual é o maior deles: ( o programa encerra quando digitar o valor {quant}')

num = int( input('\nDigite um número: '))
maior = num
menor = num
while num > quant:
    if num > maior:
        maior = num
    else:
        menor = num
    num = int( input('Digite um número: '))

print(f'O maior número é {maior}')
print(f'O menor número é {menor}')
