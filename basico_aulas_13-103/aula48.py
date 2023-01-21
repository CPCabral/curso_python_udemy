"""
Listas em Python
tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
    append - adiciona o item ao final
    insert - adiciona um item na posição escolhida
    pop - remove do final ou do indice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - stende a lista
    + - concatena a lista
Create Read Update   Delete
Criar, ler, alterar, apagar = lista [i] (CRUD)
"""

# string = 'ABCDE' # 5 caracteres (len)
# lista = [] # ''
# #          0    1          2         3    4
# lista1 = [123, True, 'Luiz otávio', 1.2, []]
# #print(bool([]))  # falsy
# lista1[-3] = 'Maria'

# print(lista1)

# lista = [10, 20, 30, 40]
# lista[2] = 300
# print(lista)
# del lista[2]
# print(lista)
# lista.append(50)
# lista.append(60)
# print(lista)
# lista.pop()
# print(lista)
# removido = lista.pop(3)
# print(lista, 'removido', removido)

lista = [10, 20, 30, 40]
lista.append('luiz')
nome = lista.pop()
lista.append(1233)
del lista[-1] 
lista.insert(0,5)
print(lista)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b)
print(lista_a)