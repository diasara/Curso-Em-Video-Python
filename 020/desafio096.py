# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular 
# (largura e comprimento) e mostre a área do terreno.

def área(largura, comprimento):
    print(f'A largura é {largura} metros e o comprimento é {comprimento} metros. A área é {largura * comprimento} m².')


largura = float(input('Qual a largura em metros? '))
comprimento = float(input('Qual o comprimento em metros? '))

área(largura, comprimento)
