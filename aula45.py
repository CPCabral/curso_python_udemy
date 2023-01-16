"""
for
iterável -> str, range, etc (__iter__)
iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue o seu iterador
"""
numeros = range(0,100,8)

for numero in numeros:
    print(numero)
