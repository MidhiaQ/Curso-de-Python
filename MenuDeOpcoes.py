n1 = int(input('Pimeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair do programa''')
    opcao = int(input('Informe sua opcao: '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma de {} e {} é {}'.format(n1,n2,soma))
    elif opcao == 2:
        produto = n1 * n2
        print('A multiplicação de {} e {} é {}'.format(n1,n2,produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior é {}'.format(n1,n2,maior))        
    elif opcao == 4:
        print('Digite os numeros novamente: ')
        n1 = int(input('Primeiro numero: '))
        n2 = int(input('Segundo nuemro: '))
    elif opcao == 5:
         print('Saindo...')              
print("Fim")    