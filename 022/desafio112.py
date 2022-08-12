# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um
# módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja
# capaz de funcionar como a função input(), mas com uma validação de dados
# para aceitar apenas valores que sejam monetários.

from utilidadesCeV import dado, moeda

n = dado.leiaDinheiro('Digite um valor monetário: ')

moeda.resumo(n, 50, True)
