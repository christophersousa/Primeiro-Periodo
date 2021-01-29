import random

nlin= 2
ncol = 3

a = [[None] * ncol for i in range(nlin)]
b = [[None] * ncol for i in range(nlin)]
c = [[None] * ncol for i in range(nlin)]

print('Matriz A')

for i in range(nlin):
    for j in range(ncol):
        a[i][j] = random.randint(1,20)

print('\nMatriz B')

for i in range(nlin):
    for j in range(ncol):
        b[i][j] = random.randint(1,20)

for i in range(nlin):
    for j in range(ncol):
        c[i][j] = a [i][j] + b[i][j]


print(f'\nMatriz A')

for i in range(nlin):
    for j in range(ncol):
        print(f'{a[i][j]:4}', end = ' ')
    print()

print(f'\nMatriz B')
for i in range(nlin):
    for j in range(ncol):
        print(f'{b[i][j]:4}', end = ' ')
    print()

print(f'\nMatriz C')
for i in range(nlin):
    for j in range(ncol):
        print(f'{c[i][j]:4}', end = ' ')
    print()
