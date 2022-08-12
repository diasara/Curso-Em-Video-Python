# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e
# vai retornar um dicionário com as seguintes informações:
#    - Quantidade de notas
#    - A maior nota
#    - A menor nota
#    - A média da turma
#    - A situação (opcional)

# Adicione também as docstrings da função.

from statistics import mean

def notas(*num, sit = False):
    dicio = {}

    dicio['Quantidade de notas'] = len(num)
    dicio['Maior nota'] = max(num)
    dicio['Menor nota'] = min(num)
    dicio['Media da turma'] = mean(num)

    if sit:
        if mean(num) > 7:
            dicio['Situação'] = 'BOA'
        elif mean(num) < 5:
            dicio['Situação'] = 'RUIM'
        else:
            dicio['Situação'] = 'RAZOÁVEL'
    
    return dicio


stats = notas(5, 3, 2, 5, 6, 9, sit = True)
print(stats)
