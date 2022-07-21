# Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que 
# é a condição de parada. No final, mostre quantos números foram digitados 
# e qual foi a soma entre eles (desconsiderando o flag).

count = 0
n = 0
soma = 0

while n != 999:
	n = int(input('Digite um número: '))
	count += 1
	soma += n

print('Você digitou {} números. A soma deles é {}.' .format(count, soma))
