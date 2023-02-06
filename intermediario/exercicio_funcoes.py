# Exercícios com funções

# Crie uma função que multiplica todos os argumentos não nomeados recebidos.
# Retorne o total para uma variável e mostre o valor da variável

def multiplica(*args):
    multiplicacao = 1
    for numero in args:
        multiplicacao *= numero
    return multiplicacao

lista = 5, 4, 7, 3, 8
resultado = multiplica(*lista)

print(f'a multiplicação entre os números {lista} = {resultado}')
    

# Crie uma fução que fala se o número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def epar(x):
    if x % 2 == 0:
        return print(f'{x} é par!')
    return print(f'{x} é ímpar!')

epar(24)
epar(25)