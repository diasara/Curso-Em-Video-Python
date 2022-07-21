# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Escreva seu nome: ')).strip().upper()

print(nome.find('SILVA'))
