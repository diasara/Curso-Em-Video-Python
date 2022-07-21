# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))

media = (n1 + n2 + n3) / 3 

if media >= 7.0:
	print('O aluno está APROVADO!')
elif media < 5.0:
	print('O aluno está REPROVADO!')
else:
	print('O aluno está de RECUPERAÇÃO!')

# Python é diferente de C. Aqui você pode colocar uma variável entre condicionais!
# Ex.: media < 7.0 and media >= 5 pode ser escrito como 7 > media >= 5.
