#Ler o comprimento de três retas e verificar se podem formar um triângulo
from time import sleep
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
print('='*20)
print('Analisando...')
print('='*20)
sleep(3)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode formar um triângulo!')
else:
    print('Não pode formar um triângulo.')