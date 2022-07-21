# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valorCasa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
tempo = int(input('Em quantos anos você pretende pagar o empréstimo? '))

prestacao = valorCasa / (tempo * 12)

if prestacao > (salario * 0.3):
	print('Empréstimo negado!')
else:
	print('Empréstimo aprovado!')
