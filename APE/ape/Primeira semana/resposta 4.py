n = input( 'Nome do cliente: ')
c = float(input('Quantidade pedida de Chocolate: '))
r = float(input('Quantidade pedida de Refrigerante: '))
m = float(input('Quantidade pedida de Misto Quente: '))
s = float(input('Quantidade pedida de Sorvete: '))

q1 = c * 4
q2 = r * 5
q3 = m * 3.50
q4 = s * 3
soma = q1+q2+q3+q4

print()
print('Cliente',n)
print()
print(' Tabela ')
print(f'\n Chocolate = R$ 4,00 pedidos: {c} valor: {q1} \n Refrigerante = R$ 5,00 pedidos: {r} valor: {q2} \n Misto quente = R$ 3,50 pedidos: {m} valor: {q3} \n Sorvete = R$ 3,00 pedidos: {s} valor: {q4}')
print()
print(f'Conta do cliente {n} = {soma}')
