print('*'*34)
print('Digite o nome para gerar um login')
print('*'*34)

nomes = input('\nNome: ').lower()

lista = nomes.split()
n = len(lista)
login = lista[0]

for i in range(1,n):
    login = login + lista[i][0]
    
print('login = ',login)
