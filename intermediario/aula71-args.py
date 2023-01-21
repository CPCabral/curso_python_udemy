"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(x, y):
    return x + y

def soma(*args):
    total = 0
    for numero in args:
        total += numero
        
    return total

numeros = 1, 2, 3, 4, 5, 6

soma123 = soma(*numeros)
print(soma123)

print(sum(numeros)) #função de soma do python