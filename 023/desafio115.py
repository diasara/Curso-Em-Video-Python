# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo
# de texto simples.

# O sistema só vai ter duas opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

try:
    nome_arquivo = 'exemplo.txt'
    arquivo = open(nome_arquivo, 'rt')
except FileNotFoundError:
    arquivo = open(nome_arquivo, 'wt+')

arquivo.close()

while True:
    print('\nFaça sua escolha:\n'
    '1 - Cadastrar um nome\n'
    '2 - Conferir os cadastrados\n'
    '3 - Sair do programa\n')
    
    decisao = str(input('Decisão: '))

    if decisao == '1':
        arquivo = open(nome_arquivo, 'at')
        nome = str(input('Insira o nome: ')).strip().title()
        arquivo.write(f'{nome}\n')
        arquivo.close()
    elif decisao == '2':
        arquivo = open(nome_arquivo, 'rt')
        print('\nNOMES CADASTRADOS')
        print(arquivo.read())
        arquivo.close()
    elif decisao == '3':
        break
    else:
        print('Opcão inválida! Tente de novo!')

# Esse foi o código que eu fiz para a questão.
# Ele não está modularizado mas é funcional.
# A pasta "desafio115" contêm o código do professor que achei melhor copiar.
