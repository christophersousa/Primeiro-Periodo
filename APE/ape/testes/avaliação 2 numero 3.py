nome = input('Nome do empregado: ')
salario = float(input(' Salário atual: '))
reajuste = salario * 20/100
salario2 = salario + reajuste
print(f'\n empregado: {nome} \n Salario atual: {salario} \n reajuste do salarial em 20%: {reajuste} \n Salario reajustado vai ser no valor de: {salario2}')
