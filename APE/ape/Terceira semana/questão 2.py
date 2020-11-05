m = int(input('Matrícula do operário: '))
p = int(input('Quantidades de peças fabricadas no mês : '))
peças = p - 30
bonus = peças * 10
sm = 1045
if p > 30:
    salario = bonus + sm
    print(f' O empregado de matrícula {m} \n classificado na classe B \n receberá um bônus salarial de R${bonus}')
    print(f' Salario = {salario: .2f}')
else:
    print(f' O empregado de matrícula {m} \n classificado na classe A \n receberá um bônus salarial de R$ 0')
    print(f' Salario = {sm: .2f}')
    
    
