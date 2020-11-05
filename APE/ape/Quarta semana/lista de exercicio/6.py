primo = True

n = int(input('Digite um número inteiro: ' ))

for i in range (2,n):
    if n % i == 0:
        primo = False
if primo:
    print(n,'é primo')
else:
    print(n,'Não é primo')

