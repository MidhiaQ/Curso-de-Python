print('PROMOÇÃO DE 5%!!')
preco = float(input('Digite o valor do produto: '))
des = preco - (preco * 5 / 100)
print('Preço antigo: {} \nNovo preço: {}'.format(preco, des))