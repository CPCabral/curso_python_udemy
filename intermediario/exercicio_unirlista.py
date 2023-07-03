# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

#opção1
def zipper(lista1, lista2):
    # if len(lista2) < len(lista1):
    #     lista1, lista2 = lista2, lista1
    
    resultado = []
    for i in range(min(len(lista1),len(lista2))):
        resultado.append((lista1[i], lista2[i]))
    return resultado

#opção2
def zipper2(lista1, lista2):
    
    return [(lista1[i], lista2[i]) for i in range(min(len(lista1),len(lista2)))]

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']

print(zipper(cidades,estados))
print()
print(zipper2(cidades,estados))
print()

#opção3
print(list(zip(cidades,estados)))
print()

#opção4
#usando a lista maior
from itertools import zip_longest
print(list(zip_longest(cidades,estados)))