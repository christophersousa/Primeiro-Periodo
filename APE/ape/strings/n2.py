print('*'*62)
print('Digite um verbo regular para que seja gerada a sua conjugação.')
print('*'*62)
while True:
    
    verbo = input('\nVerbo: ').lower()

    
    cont = len(verbo)
    dim = cont-2
    saida = verbo[0:dim]
    ind = verbo[dim:]

    if ind == 'ar':
        eu = saida + 'o'
        tu = saida + 'as'
        ele = saida + 'a'
        nos = saida + 'amos'
        vos = saida + 'ais'
        eles = saida + 'am'
        
    if ind == 'er':
        eu = saida + 'o'
        tu = saida + 'es'
        ele = saida + 'e'
        nos = saida + 'emos'
        vos = saida + 'eis'
        eles = saida + 'em'

    if ind == 'ir':
        eu = saida + 'o'
        tu = saida + 'es'
        ele = saida + 'e'
        nos = saida + 'imos'
        vos = saida + 'is'
        eles = saida + 'em'
        
    print()    
    print('-'*15)
    
    print(f'Eu =   {eu}')
    print(f'Tu =   {tu}')
    print(f'Ele =  {ele}')
    print(f'Nós =  {nos}')
    print(f'Vós =  {vos}')
    print(f'Eles = {eles}')
    
    print('-'*15)

    perg = input('\nDeseja continuar? ').upper()

    if perg == 'NÃO' or perg == 'NOT' or perg == 'FIM' or perg == 'N':
        break

    if perg != 'SIM' and perg != 'S' and perg != 'YES' and perg != 'CONTINUAR':
        print('Erro de interpretação, Digite novamente !!!')
        continue
    
print('\nObrigado por sua participação!!!')
