# Manipulando texto

frase = 'Curso em Vídeo Python' # Cada caractere é separado na memória / Fatiamento
# frase[9] # O caractere na posição 9
frase[9:13] # O caractere na posição 9 até o caractere na posição 12.
frase[9:21] # O caractere na posição 9 até o caractere na posição 20.
frase[9:21:2] # Pula de dois em dois caracteres. 9 - 11 - 13 - 15 - 17 - 19
frase[:5] # É a mesma coisa que escrever frase[0:5]
frase[15:] # Começa no caractere 15 até o final da string.
frase[9::3] # Começa no caractere 9, vai até o final e pula de três em três.

# Análise da string

len(frase) # Indica o comprimento da string.
frase.count('o') # Faz a contagem de quantas vezes a palavra 'o' aparece na string (pode escolher outra letra, claro).
frase.count('o', 0, 13) # Estabelece uma posição mínima e máxima para conferir se tem a letra 'o'.
frase.find('deo') # Em que momento começa o 'deo'.
frase.find('Android') # Se você coloca dentro do find uma palavra que não existe na string, ele retorna o valor -1.
'Curso' in frase # Verifica se existe 'Curso' na string. Se houver, ele retorna True; senão, False. / 'in' é um operador.

# Tranformação da string

frase.replace('Python', 'Android') # Substitui, de forma secundária, a palavra 'Python' por 'Android'
frase.upper() # Coloca todos os caracteres em maiúsculo.
frase.lower() # Coloca todos os caracteres em minúsculo.
frase.capitalize() # Vai colocar todas as letras da string em minúsculo, com exceção da primeira letra que vai ficar em maiúsculo.
frase.title() # Analiza quantas palavras existem na string (com base nos espaços) e coloca toda primeira letra das palavras em maiúsculo.
frase.strip() # Remove os espaços desnecessários na string.
frase.rstrip() # Remove somente os últimos espaços da string.
frase.lstrip() # Remove somente os primeiros espaços da string.

# Divisão e junção

frase.split() # Divide a string de acordo com os espaços. Ele gera uma lista.
'-'.join(frase) # Junta todos os elementos de frase e coloca um '-' entre as palavras.

# Bônus

print(""" Texto super longo que ocupa linhas diferentes""")

# Válido saber: uma string, nos seus micro-elementos, é imutável; a não ser que se utilize uma função de transformação de string e use uma atribuição
frase = frase.replace('Python', 'Android')
# Você pode usar essas funções dentro de print's sem precisar usar a atribuição.

dividido = frase.split()
print(dividido[2][3]) # Pega o dividido[2] = 'Vídeo' e imprime o seu terceiro caractere.