#Para que não fique um programa muito grande optei por deixar o usuario definir quantos jogos seram análisados#

flag = int(input('Quantos jogos seram análisados: '))
vit_pri = 0
vit_seg = 0
empate = 0
total_gols = 0

for i in range(1, flag+1):
    pri_time = input('\nTime mandante: ')
    seg_time = input('Time visitante: ')
    plac_pri = int(input('Quantidade gols marcado pelo time mandante: '))
    plac_seg = int(input('Quantidade gols marcado pelo time visitante: '))

    if plac_pri > plac_seg:
        vit_pri = vit_pri + 1

    elif plac_pri == plac_seg:
        empate = empate + 1
        
    else:
        vit_seg = vit_seg + 1

    total_gols = total_gols + (plac_pri + plac_seg)

print(f'\nVitorias conquistadas pelos mandante dos jogos foram: {vit_pri}')
print(f'Vitorias conquistadas pelos visitantes do jogos foram: {vit_seg}')
print(f'Empates da rodada: {empate}')
print(f'Total de gols marcados na rodada: {total_gols}')
