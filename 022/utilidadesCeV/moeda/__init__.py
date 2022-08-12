def resumo(n = 0, p = 0, mon = False):
    '''
    -> Aplica todas as funções
    :param n: número recebido.
    :param p: porcentagem a ser aplicada.
    :return: não retorna nada.
    '''
    print(f'O número {moeda(n)} aumentado em {p}% é igual a {aumentar(n, p, mon)}')
    print(f'O número {moeda(n)} diminuído em {p}% é igual a {diminuir(n, p, mon)}.')
    print(f'O dobro de {moeda(n)} é {dobro(n, mon)}.')
    print(f'A metade de {moeda(n)} é {metade(n, mon)}.')


def moeda(n = 0):
    '''
    -> Mostra o valor recebido como valor monetário.
    :param n: número a ser formatado.
    :return: retorna o texto formatado.
    '''
    return f'R$ {n:.2f}'


def aumentar(n = 0, p = 0, mon = False):
    '''
    -> Aumenta o valor recebido em X %.
    :param n: número a ser formatado.
    :param p: porcentagem a ser somada.
    :param mon: opção sobre o valor ser apresentado monetizado.
    :return: retorna o resultado.
    '''

    r = n + n * (p / 100)

    if mon:
        return moeda(r)
    else:
        return f'{r:.2f}'


def diminuir(n = 0, p = 0, mon = False):
    '''
    -> Diminui o valor recebido em X %.
    :param n: número a ser formatado.
    :param p: porcentagem a ser diminuída.
    :param mon: opção sobre o valor ser apresentado monetizado.
    :return: retorna o resultado.
    '''

    r = n - n * (p / 100)

    if mon:
        return moeda(r)
    else:
        return f'{r:.2f}'


def dobro(n = 0, mon = False):
    '''
    -> Dobra o valor recebido.
    :param n: número a ser dobrado.
    :param mon: opção sobre o valor ser apresentado monetizado.
    :return: retorna o resultado.
    '''

    r = n * 2

    if mon:
        return moeda(r)
    else:
        return f'{r:.2f}'


def metade(n = 0, mon = False):
    '''
    -> Dividi o valor recebido pela metade.
    :param n: número a ser dividido.
    :param mon: opção sobre o valor ser apresentado monetizado.
    :return: retorna o resultado.
    '''

    r = n / 2

    if mon:
        return moeda(r)
    else:
        return f'{r:.2f}'
