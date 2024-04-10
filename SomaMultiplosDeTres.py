#calcule a soma entre todos os números ímpares que são múltiplos de três no intervalo de 1 até 500
soma = 0
for cont in range(1,501, 2):
    if cont % 3 == 0:
        soma = soma + cont
print('A soma é = {}'.format(soma))        