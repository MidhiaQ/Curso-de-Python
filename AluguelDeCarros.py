dias = int(input('Quantos dias foi alugado?'))
km = float(input('Quantos KM foram rodados?'))

pagar = (dias * 60) + (km * 0.15)
print('Valor: {:.2f}R$'.format(pagar))