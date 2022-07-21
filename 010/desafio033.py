# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
num3 = float(input('Digite um último numero: '))

if num1 > num2 and num1 > num3:
	maior = num1
	menor = num2 if num2 < num3 else num3
elif num2 > num1 and num2 > num3:
	maior = num2
	menor = num1 if num1 < num3 else num3
else:
	maior = num3
	menor = num1 if num1 < num2 else num2
	
print('O menor número é {:.2f} e o maior é {:.2f}.' .format(menor, maior))
