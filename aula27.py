"""
Fatiamento de strings
012345678
Olá mundo

Fatiamento [i:f:p] [::]

Obs.: a função len retorna a quantidade de itens da str
"""
variavel = "Olá mundo"
print(variavel[-4])
print(variavel[4:])
print(variavel[4:7]) #INDICE final NÃO É INCLUÍDO 
print(variavel[:4]) 

tamanho = len(variavel)
print(tamanho)
print(variavel[4:tamanho])

#passo
print(variavel[0:tamanho:2])
print(variavel[0:tamanho:-1])
