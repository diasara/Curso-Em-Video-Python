# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

s = str(input('Qual o seu sexo? [M/F] ')).upper().strip()

print(s)

while s != 'M' and s != 'F':
	s = str(input('''Opção inválida!
Qual o seu sexo? [M/F]'''))

if s == 'M':
	s = 'MASCULINO'
else:
	s = 'FEMININO'
	
print('Seu sexo é {}.' .format(s))
