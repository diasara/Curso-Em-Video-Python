# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = str(input('Escreva o seu nome completo: '))

print(nome.upper())
print(nome.lower())

nome = nome.split()
print(len(nome) - nome.count(' '))
print(len(nome[0]))
