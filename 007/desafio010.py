# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quatos dólares ela pode comprar. Considere US$1.00 = R$3.27

n1 = float(input('Quanto dinheiro você tem na sua carteira? R$ '))

print('Você tem o equivalente a US${:.2f} na sua carteira.' .format(n1 / 3.27))