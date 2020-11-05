
INSS = 12/100
totalSB = 0
totalD = 0
totalSL = 0

linha = '-' * 32
quant = int( input('Quantidade de funcionarios será analisado : '))
for i in range(quant):
    nome = input('\nNome do funcionario: ').title()
    salarioB = float(input('Valor do salário Bruto: '))
    
    salario_bruto = salarioB
    
    if salario_bruto > 1045:   
        desconto = salario_bruto * INSS
        salarioL = salario_bruto - desconto
        
    else:
        salario_bruto = 1045
        desconto = salario_bruto * INSS
        salarioL = salario_bruto - desconto

    totalSB = totalSB + salario_bruto 
    totalD = totalD + desconto
    totalSL = totalSL + salarioL
    
    
    print(f'\nfuncionario {nome} \nSalário Bruto: {salario_bruto: .2f} \nDesconto do INSS (12%): {desconto: .2f} \nSalario Liquido {salarioL: .2f}')
    print(linha)
print(f'\nSoma total do salario Bruto: {totalSB:.2f} \nSoma total dos descontos INSS: {totalD:.2f} \nSoma total do salario Liquido: {totalSL:.2f}')
    
