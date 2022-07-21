# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import sqrt, pow

catop = float(input('Digite o valor do cateto oposto: '))
catad = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = sqrt(pow(catop, 2) + pow(catad, 2))

print('O valor da hipotenusa é {}' .format(hipotenusa))

# Dá pra fazer com apenas uma função da biblioteca math.

from math import hypot

hipotenusa = hypot(catop, catad)

print('O valor da hipotenusa é {}' .format(hipotenusa))


