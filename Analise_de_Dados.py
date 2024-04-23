total18 = totalH = totalM20 = 0

while True:
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]

    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        totalH += 1
    if sexo == 'F' and idade < 20:
        totalM20 += 1
    
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]

    if resposta == 'N':
        break

print(f'Total de pessoas com mais de 18: {total18}')
print(f'Total de homens cadastrados: {totalH}')
print(f'Mulheres com menos de 20 anos: {totalM20}')
