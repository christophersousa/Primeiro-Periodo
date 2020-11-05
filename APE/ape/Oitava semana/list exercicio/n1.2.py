n = int(input('Quantas vezes será analisado; '))
a = [None]*n
b = [None]*n
k = 5

for i in range(n):
    num = int(input(f'{i + 1}°= '))
    a[i]= num
    b[i]= a[i] * k

print(a)
print(b)
