# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'l1': [0, 1, 2]
}

print(pessoa.__len__())
print(len(pessoa))

print(pessoa.keys())
print(list(pessoa.keys()))

print(list(pessoa.values()))

print(list(pessoa.items()))
for chave, valor in pessoa.items():
    print(chave,valor)

pessoa.setdefault('endereço', 'juquitiba')

d1 = pessoa 
d1['idade'] = 25

d2 = pessoa.copy() # shallow copy
d2['idade'] = 18
d2['l1'][1] = 9999

print(pessoa)
print(d2)

import copy
d3 = copy.deepcopy(pessoa) # shallow copy
d3['idade'] = 21
d3['l1'][1] = 10

print(pessoa)
print(d2)
print(d3)

nome = pessoa.pop('nome')
print(pessoa)

ultima_Chave = pessoa.popitem()
print(pessoa)

pessoa.update({
    'nome': 'novo valor',
    'idade': 20,
})

print(pessoa)

pessoa.update(nome='Camila', idade= 30)
print(pessoa)

tupla = (('nome', 'novo valor'),('idade', 35))
lista = [['nome', 'novo valor'],['idade', 35]]

pessoa.update(tupla)
pessoa.update(lista)
