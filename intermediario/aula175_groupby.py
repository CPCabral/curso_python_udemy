# goupby - agrupando valores (itertools)
from itertools import groupby

# alunos = ['a','a','a','a', 'b', 'c', 'b']
# grupos = groupby(sorted(alunos))
# # print(grupos)
# # print(list(grupos))

# for chave, grupo in grupos:
#     print(chave)
#     print(list(grupo))

########################################

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]
# alunos_agrupados = sorted(alunos, key = lambda a: a['nota'])

# grupos = groupby(alunos_agrupados, key = lambda a: a['nota'])
def ordena(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key = ordena)

grupos = groupby(alunos_agrupados, key = ordena)

for chave, grupo in grupos:
    print('nota ',chave)
    print(*list(grupo), sep = '\n')