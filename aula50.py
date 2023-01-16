#Introdução ao desempacotamento + Tuples

nomes = ['Maria', 'Helena', 'Luiz']

# nome1, nome2, nome3 = nomes
# print(nome2)

nome1, *resto = nomes
print(nome1, resto)

nome1, *_ = nomes
print(nome1)


_, nome2, *_ = nomes
print(nome2)