"""
split e join com list e str
split - divide uma sting
join - une em uma string
"""
frase = 'olha só que, coisa interessante'
lista_palavras = frase.split(', ')
print(lista_palavras)

#.strip() corta espaços do começo e fim
frases_unidas = '-'.join(lista_palavras)
print(frases_unidas)