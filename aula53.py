#enumerate - enumera iteráveis (índices)

nomes_lista = ['Maria', 'Helena', 'Luiz']
nomes_lista.append('João')

lista_enumerada = list(enumerate(nomes_lista))

for item in enumerate(nomes_lista):
    #indice,nome = item
    print(item)

for indice,nome in enumerate(nomes_lista):
    #indice,nome = item
    print(indice,nome)

#depois do for ele consome o enumerate
print(lista_enumerada)