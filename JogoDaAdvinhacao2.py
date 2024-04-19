from random import randint

compu = randint(0, 10) #sortear os números
print('*' * 35)
print('Pense em um numero entre 0 e 10...')
print('*' * 35)
acertou = False
tentativas = 0
while not acertou:
    jogador = int(input('Tente advinhar o numero:'))
    tentativas += 1
    if jogador == compu:
        acertou = True
    else:
        if jogador < compu:
            print('Mais... Tente novamente')
        elif jogador > compu:
            print('Menos... Tente novamente')        
print("Voce acertou com {} tentativas".format(tentativas))