import random

n = int( input('Digite a ordem da matriz: '))

a = [[None] * n for i in range(n)]



for i in range(n):
    for j in range(n):
        a[i][j] = random.randint(1,20)

print(f'\nMatriz A')
for i in range(n):
    for j in range(n):
        if i == j:
            a[i][j] = 0
            
        if i>j:
            a[i][j] = i
            
        if i < j:
            a[i][j] = j
            
        print(f'{a[i][j]:4}', end = '')
    print()

print(f'\n Diagonal principal')
for i in range(n):
    for j in range(n):
        if i == j:
            a[i][j] = 0
            print(f'{a[i][j]:4}', end = '')
