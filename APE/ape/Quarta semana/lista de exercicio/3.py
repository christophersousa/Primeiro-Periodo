pm = 0
pf = 0
n = int(input('Quantidade de pessoas intrevistadas: '))
for i in range(n):
    
    sexo = input('\nSexo(M/F): ').upper()
               
    if sexo == 'M':
        pm = pm + 1
    else:
        pf = pf + 1
        
    total = pm + pf
    percM = pm / total * 100
    percF = pf / total * 100

    print(f'Percentual de homens: {percM:.0f}%')
    print(f'Percentual de mulheres: {percF:.0f}%')
               
            
