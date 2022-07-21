# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians
ang = float(input('Digite o valor do ângulo: '))

seno = sin(radians(ang))
print('Seno de {}° = {:.2f}' .format(ang, seno))

cosseno = cos(radians(ang))
print('Cosseno de {}° = {:.2f}' .format(ang, cosseno))

tangente = tan(radians(ang))
print('Tangente de {}° = {:.2f}' .format(ang, tangente))
