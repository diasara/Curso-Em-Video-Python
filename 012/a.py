# Condições Aninhadas

carro.siga()
if carro.esquerda():
	bloco_de_comando_1
elif carro.direita(): # Pode-se usar quantos "elif" quiser.
	bloco_de_comando_2
else:
	bloco_de_comando_3
	
nome = str(input('Qual é o seu nome?')).capitalize().strip()
if nome == 'Gustavo':
	print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo'
	print('Seu nome é bem popular!')
else:
	print('Seu nome é bem normal.')
print('Seja bem-vinde, {}!' .format(nome))
