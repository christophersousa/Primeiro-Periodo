s = 0
n = int(input('Digite um número: '))
for i in range(1,n+1):
    s = i + s
    print(i, end=' ')
    if n > i:
        print('+' , end=' ')
    else:
        print('=', end=' ')
print(s)
