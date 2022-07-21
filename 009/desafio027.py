# Faça um programa que leia o nome completo de uma pessoa, 
# mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Escreva o seu nome completo: ')).title().strip()

nome = nome.split()

print(nome[0])
print(nome[int(len(nome)) - 1])
