"""
Interpolção básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (0123456789ABCDEF)
"""
nome = 'Luiz'
preco = 1000.95897643
variavel = 'Luiz, o preço total foi de R$ 1000.96'
variavel1 = '%s, o preço total foi de R$ %.2f' % (nome, preco)
print(variavel)
print(variavel1)

print('O hexadecimal de %d é %X' % (1500,1500))
