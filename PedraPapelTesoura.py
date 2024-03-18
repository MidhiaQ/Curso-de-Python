from random import randint
item = ('Pedra', 'Papel', 'Tesoura')
compu = randint (0, 2)
print('''Opções:
      [0] Pedra
      [1] Papel
      [2] Tesoura''')
print('='*23)
jogador = int(input('Escolha uma das opções: '))
print('Computador - {}'.format(item[compu]))
print('Jogador - {}'.format(item[jogador]))
print('='*23)

if compu == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador vence')
    elif jogador == 2:
        print('Computador vence')
    else:
        print('ERRO')            
elif compu == 1:
    if jogador == 0:
        print('Computador vence')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador vence')
    else:
        print('ERRO')            
elif compu == 2:     
    if jogador == 0:
        print('Jogador vence')
    elif jogador == 1:
        print('Computador vence')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('ERRO')                



