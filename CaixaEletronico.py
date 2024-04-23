#Considere que o caixa possui cedulas de 50, 20, 10 e 1
BANCO = 'BANCO'

print('=' * 35)
print('{:^35}'.format(BANCO))
print('=' * 35)

valor = int(input('Qual valor deseja sacar:'))

total = valor
ced = 50
totalced = 0

while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'O total de {totalced} cedulas de {ced}')
        if ced == 50:
            ced =  20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('=' * 35)
print('Acabou')                