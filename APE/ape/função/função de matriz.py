import random

def diagonal_p(v):
    
    vetor = [None]* len(v)
    
    for i in range(len(v)):
        for j in range(len(v)):
            if i == j:
                vetor[i] =+ v[i][j]
    return vetor





n = int(input('Digite a ordem quadrada da matriz: '))

a = [[None]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        a[i][j] = random.randint(1,10)


print('\nMatriz:')
print()
print('*'*15)
print()

for i in range(n):
    for j in range(n):
        print(f'{a[i][j]:4}', end = ' ')
    print()
    
print()
print('*'*15)

diagonalp = diagonal_p(a)

print('\nDiagonal Principal:')
print()

print('*'*10)
print('\n',diagonalp)
print()
print('*'*10)
