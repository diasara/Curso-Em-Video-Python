# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e 
# a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Qual foi a quantidade de quilômetros rodados? '))
dias = int(input('Qual foi a quantidade pelos quais ele foi alugado? '))

preco = dias * 60 + km * 0.15

print('Foram rodados {} quilômetros e o carro foi alugado por {} dias.' .format(km, dias))
print('O preço a pagar é de R$ {:.2f}.' .format(preco))