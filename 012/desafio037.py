# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 
# 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número: '))
print('Você quer converter esse número para qual base?')
base = int(input('(1) Binário (2) Octal (3) Hexadecimal\n'))

if base == 1:
	conv = bin(num)
elif base == 2:
	conv = oct(num)
elif base == 3:
	conv = hex(num)
else:
	print('Opção inválida.')
	
if base > 0 and base < 4:
	print(conv[2:])
