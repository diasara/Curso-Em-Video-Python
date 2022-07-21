# Crie um programa que tenha uma tupla totalmente preenchida com 
# uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e
# mostrá-lo por extenso.

tupla = ('zero', 'um', 'dois', 'três', 'quatro',
         'cinco', 'seis', 'sete', 'oito', 'nove',
         'dez', 'onze', 'doze', 'treze', 'catorze',
         'quinze', 'dezesseis', 'dezessete', 'dezoito',
         'dezenove', 'vinte', 0)

while True:
  num = int(input('\nDigite um número entre 0 e 20: '))

  if 0 <= num <= 20:
    print(f'\nVocê digitou o número {tupla[num]}.')
    
    continuar = ' '

    while continuar not in 'SN':
      continuar = str(input('\nVocê quer continuar? [S/N]')).upper()[0]

    if continuar == 'N':
      break
      