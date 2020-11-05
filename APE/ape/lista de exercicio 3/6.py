import math
print('Vamos calcular uma equação de segundo grau? \nDigite em sequencia a seguinte equação a + b² - c = 0')
a = int(input('Digite o número de A: '))
b= int(input('Digite o número de B: '))
c = int(input('Digite o número de C: '))
delta = (b**2) - (4 * a * c)

if delta < 0:
    print('Não existe raiz')
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f'o resultado de x¹ é {x1:.1f} e o de x² é {x2:.1f}')
