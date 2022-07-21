#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input('Digite o seu salário atual: '))

print('A partir de agora, o seu salário será de R${}.' .format(s + (s * 0.15)))