# combinations peermutations and Product - Itertools
# Combinação - ordem não importa - iteravel + tamanho do grupo
# Permutação - ordem importa
# produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product

pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia'
    ]
camisetas = [
    ['preta', 'branca'],
    ['p','m','g'],
    ['masculino','feminino']
    ]

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

print('Combination:')
print_iter(combinations(pessoas,2))
print('Permutation:')
print_iter(permutations(pessoas,2))
print('Product:')
print_iter(product(*camisetas))

