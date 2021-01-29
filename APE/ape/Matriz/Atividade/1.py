import random

ordem = int ( input('Digite a ordem da Matriz: '))

a = [[None]*ordem for i in range(ordem)]
b = [[None]*ordem for i in range(ordem)]

aux = ordem - 1
#Leitura dos índices da Matriz A#
for i in range(ordem):
    for j in range(ordem):
        a[i][j] = random.randint(1,10)

#Gerador dos índices da Matriz B#
for i in range(ordem):
    for j in range(ordem):
        b[i][j] = a[i][j] + (i+j)
        
        #Diagonal Principal#
        if i == j:
            b[i][j] = 0
            
        #Diagonal Secundaria#
        if i == ordem-j-1:
            b[i][j] = 0

        
#Matrizes#
print(f'\nMatriz A')
for i in range(ordem):
    for j in range(ordem):
        print(f'{a[i][j]:4}', end = '')
    print()

print(f'\nMatriz B')
for i in range(ordem):
    for j in range(ordem):
        print(f'{b[i][j]:4}', end = '')
    print()
