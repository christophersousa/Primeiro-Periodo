n = int(input('N = '))
x = int(input('X = '))
y = int(input('Y = '))

print(f'Os multiplos do número {n} entre os números {x} e {y} são:')

for i in range(x,y+1):
    if i % n == 0:
        print(i, end= ' ')
    
    
