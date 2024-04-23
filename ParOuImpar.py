from random import randint

v = 0
while True:
    jogador = int(input('Digite um valor: '))
    compu = randint(0, 10)
    total = jogador + compu
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar: [P/I]')).strip().upper()[0]
    print(f'Jogador {jogador} e computador {compu}. Total {total}')
    print('Par' if total % 2 == 0 else 'Impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('PERDEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('PERDEU')
            break
        print(f'GAMER OVER. Você venceu {v} vezes.')
            