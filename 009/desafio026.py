# Faça um programa que leia uma frase pelo teclado e mostre:
# - quantas vezes aparece a letra "A"; 
# - em que posição ela aparece a primeira vez;
# - e em que posição ela aparece a última vez.

frase = str(input('Escreva uma frase: ')).upper().strip()

print('A letra "A" aparece {} vezes na frase.' .format(frase.count('A')))
print('Aparece pela primeira vez na posição {} da string.' .format(frase.find('A')+1))
print('Aparece pela última vez na posição {} da string.' .format(frase.rfind('A')+1))

