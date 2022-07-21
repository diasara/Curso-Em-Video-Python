# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

valor = float(input('Qual o valor do produto? R$'))

print('Como você quer pagar?')
opcao = int(input('''	
	( 1 ) À vista em dinheiro ou cheque.
	( 2 ) À vista no cartão.
	( 3 ) No cartão, em 2x sem juros.
	( 4 ) No cartão, em 3x ou mais vezes com juros.'''))
	
if opcao == 1:
	valorfinal = valor - (valor * 0.1)
elif opcao == 2:
	valorfinal = valor - (valor * 0.05)
elif opcao == 3:
	valorfinal = valor
elif opcao == 4:
	valorfinal = valor + (valor * 0.2)
else:
	print('Opção inválida!')
	valorfinal = valor
	
if 0 < opcao < 5:
	print('O valor final é de R${:.2f}' .format(valorfinal))
