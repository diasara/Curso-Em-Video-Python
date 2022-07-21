# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Escreva o nome de uma cidade: ')).strip().upper()

print(cidade.upper().find('SANTO'))

print('SANTO' in cidade)

print(cidade[:5].upper() == 'SANTO')