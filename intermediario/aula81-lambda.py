# Função lambda em Python
 #A função lambda é uma função como qualquer outra em Python. Porém, são funções anônimas que contém apenas uma linha, ou seja, tudo deve ser contido dentro de uma única expressão.

# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]
# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort(reverse=True)
# sorted(lista)


# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
#lista.sort() #ordena a lista
# lista.sort(reverse=True) #ordena a lista decrescente
# sorted(lista)

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# def ordena(item):

#     return item ['nome']

# lista.sort(key = ordena)

# for item in lista:
#     print(item)

# def ordena(item):

#     return item ['nome']

# lista.sort(key = lambda item: item['nome'])
l1 = sorted(lista, key = lambda item: item['nome']) #copia rasa
l2 = sorted(lista, key = lambda item: item['sobrenome'])

def exibir(lista):
    for item in lista:
        print(item)

exibir(l1)
print()
exibir(l2)
l1 = [1, 2, 3]
l1.