from random import randint

compu = randint(0, 5) #sortear os números
print('*' * 35)
print('Pense em um numero entre 0 e 5...')
print('*' * 35)
jogador = int(input('Tente advinhar o numero:'))

if jogador == compu:
 print("PARABENS, VOCE ACERTOU!")
else:
 print('Voce errou, o numero era {}'.format(compu))