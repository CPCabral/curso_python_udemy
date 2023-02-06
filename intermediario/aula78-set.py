'''
Sets - Conjuntos em Python
são mutáveis mas só aceitam tipos imutáveis como valor interno.

Criando um set:
set(item1, item2, item3) ou {item1, item2, item3}

Sets são eficientes para remover valores duplicados de iteráveis
 - eles não tem indexes;
 - eles não garantesm ordem;
 - eles são iteráveis (for, in, not in)


Métodos úteis:
add, update, clear, discard
'''
# s1 = set('Camila')
# print(s1)
# s2 = {'Camila'}
# print(s2)

# l1 = [1, 2, 3, 3, 3, 3, (123,)]
# s1 = set(l1)
# l2 = list(s1)
# print(l2)
# print(3 in s1)

# MÉTODOS:

# s1 = set()
# s1.add('Camila')
# s1.add(1)
# s1.update('Olá Mundo')
# # s1.clear()
# s1.discard('Camila')
# print(s1)

# Operadores

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2 # união
s4 = s1 & s2 # intersecção
s5 = s1 - s2 # diferença - itens disponíveis apenas no primeito set
s6 = s2 - s1 # diferença - itens disponíveis apenas no primeito set
s7 = s1 ^ s2 # diferença simétrica - itens não presentes em ambos s5 | s6

print(s3)
print(s4)
print(s5)
print(s6)
print(s7)

# Exemplo de uso

letras = set()

while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    print(letras)

