#leia o nome, idade e sexo de 4 pessoas. mostre a média da idade do grupo
#nome do homem mais velho e quantas mulheres tem menos de 20 anos.
somaidade=0
mediaidade=0
maioridadehomem=0
nomevelho=''
totalmulher=0
for pessoa in range(1, 5):
    print('--------{}º Pessoa--------'.format(pessoa))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]'))
    somaidade += idade
    if pessoa == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totalmulher += 1        
mediaidade = somaidade / 4
print('Media das idades é = {}'. format(mediaidade))
print('Homem mais velho é {} tem {} anos'.format(nomevelho, maioridadehomem))
print('Mulheres com menos de 20 anos são {}'.format(totalmulher))


