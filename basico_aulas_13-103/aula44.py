"""
for + range
range -> range(start, stop, step)
"""

numeros = range(10) #passando que quer números de 0-10
# numeros = range(5,10) #de 5 - 10
# numeros = range(5,10,2) #de 5 - 10 pulando 2

for numero in numeros:
    print(numero) #ultimo digito não é incluído
