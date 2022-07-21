# Cores no Terminal

# Padrão ANSI

033[STYLE;TEXT;BACKm 
\033[0;33;44m

# Style
# 0 - nenhum; 1 - negrito; 4 - sublinhado; 7 - inverter as configurações.

# Text
# 30 - branco; 31 - vermelho; 32 - verde; 33 - amarelo; 34 - azul; 35 - lilás; 36 - ciano; 37 -  cinza

# Back // Background
# 40 - branco; 41 - vermelho; 42 - verde; 43 - amarelo; 44 - azul; 45 - lilás; 46 - ciano; 47 - cinza

\033[0;30;41m # Letra branca e fundo vermelho.
\033[4;33;44m # Letra sublinhada amarela e fundo azul.
\033[1;35;43m # Letra lilás em negrito e fundo amarelo.
\033[30;42m   # Letra branca e fundo verde. Por padrão do terminal, quando não se especifica o estilo da letra, se entende como "letra normal".
\033[m 	      #Configuração padrão do terminal é letra cinza e fundo preto.
\033[7;30m    # O que era letra branca e fundo preto vira letra preta e fundo branco.

print('\033[31;44Olá, mundo!') # Desse jeito, a cor se estende pela linha toda. Caso queira que ela se limite apenas as letras, coloque "\033[m" no final.

a = 3
b = 5
print('Os valores são \033[35m{}\033[m e \033[31m{}\033[m!!!' .format(a, b))

nome = 'Guanabara'
print('Olá, prazer te conhecer, {}{}{}' .format('\033[4;34m', nome, '\033[m'))

cores = {   'limpa'			:'\033[m',
			'azul'			:'\033[34m', 
			'amarelo'		:'\033[33m', 
			'pretoebranco'	:'\033[7:30m'}

print('Olá, prazer te conhecer, {}{}{}' .format('amarelo', nome, 'limpa'))

# Se quiser, procure sobre "colorize".