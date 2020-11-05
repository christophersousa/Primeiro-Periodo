quan = int(input('Digite a quantidade de pessoas que serão analisadas: '))

quantM = 0
quantF = 0

CM = 0
SF = 0

total = 0



print(f'\nNessa pesquisa vamos analizar {quan} pessoas e definir uma percentual entre elas')

for i in range(quan):

    sexo = input('\nSexo (M/F): ').upper()
    idade = int(input('Idade: '))
    Ec = input('Estado civil(S, C, V ou D): ').upper()

    if sexo == 'M':
        quantM = quantM + 1 
        if Ec == 'C' and idade > 30:     
            CM = CM + 1
    elif sexo == 'F':
        quantF = quantF + 1
        if Ec == 'S' and idade < 20:
            SF = SF + 1
    else:
        print('Digite as informações corretamente')
            
        
    total = quantM + quantF
    percM = quantM / total * 100
    percF = quantF / total * 100

    
    
    if CM == 0 and SF == 0:
        percM2 = 0
        percF2 = 0
        casado = 0
        solteira = 0
    else:
        percM2 = (CM / total * 100) 
        percF2 = (SF / total * 100) 
        casado = CM
        solteira = SF
        
    print(f'\nPercentual de homens: {percM:.0f}%')
    print(f'Percentual de muheres: {percF:.0f}%')
    print(f'Homens casados com idade superior a 30 anos : {casado}\n Mulheres solteiras com idade inferior a 20: {solteira}')
          
print(f'\nPercentual de homens casados com idade superior a 30: {percM2:.0f}%')
print(f'Percentual de muheres solteiras com idade inferior a 20: {percF2:.0f}%')
