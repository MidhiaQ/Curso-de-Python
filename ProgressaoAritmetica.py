#leia o primeiro termo e a razão de uma progressão aritmética. 
#no final, mostre os 10 primeiros termos dessa progressão
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for num in range(primeiro, decimo + razao, razao):
    print('{}'.format(num), end='_ ')
print("FIM")    