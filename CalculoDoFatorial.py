#from math import factorial
#num = int(input('Digite um numero:'))
#f = factorial(num)
#print('O fatorial de {} é {}'.format(num,f))
num = int(input('Digite um numero:'))
contador = num
fat = 1
print('Calculando {}! = '.format(num), end='')
while contador > 0:
    print('{}'.format(contador), end='')
    print('x' if contador > 1 else '=', end='')
    fat = fat * contador  
    contador -= 1
print('{}'.format(fat))