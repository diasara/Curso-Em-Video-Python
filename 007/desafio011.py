# Faça um programa que calcule a área de uma parede em metros e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

print('A área da parede é {} metros quadrados, e para pinta-la totalmente, é necessário {} litros de tinta.' .format(largura * altura, (largura * altura) / 2))