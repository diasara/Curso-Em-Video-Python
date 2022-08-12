# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o
# ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem
# voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

def voto(nasc):
    from datetime import datetime

    agora = datetime.now()

    if (agora.year - nasc) < 18:
        return 'NEGADO'
    elif (agora.year - nasc) > 70:
        return 'OPCIONAL'
    else:
        return 'OBRIGATÓRIO'

ano  = int(input('Qual o ano de nascimento? '))
print(f'Você nasceu em {ano}. Voto: {voto(ano)}.')
