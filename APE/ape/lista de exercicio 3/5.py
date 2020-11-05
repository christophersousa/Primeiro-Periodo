nome = input('Nome do funcionario: ').title()
venda = float(input('Valor total de vendas: '))
comissão = venda * 0.05
sm = 1045
if comissão > sm:
    print(f'Funcionario {nome}')
    print(f'Salário: {comissão}')
else:
    print(f'Funcionario {nome}')
    print(f'Salário: {sm}')
    
