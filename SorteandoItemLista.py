from random import choice
n1 = str(input('Nome:'))
n2 = str(input('Nome:'))
n3 = str(input('Nome:'))
n4 = str(input('Nome:'))
lista = [n1, n2, n3, n4]
escolhe = choice(lista)
print('Nome {}'.format(escolhe))