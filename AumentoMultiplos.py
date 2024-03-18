salario = float(input('Informe seu salario atual: '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
    print('Salario atual = {:.2f} Novo salario = {:.2f}'.format(salario, novo))
else:
    novo = salario + (salario * 10 / 100)
    print('Salario atual = {:.2f} Novo salario = {:.2f}'.format(salario, novo))