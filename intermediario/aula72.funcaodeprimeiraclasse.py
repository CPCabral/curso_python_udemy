"""
Higher Order Functions
Funções de primeira classe
Higher Order Functions - Funções que podem receber e/ou retornar outras funções

First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

passar funções como argumentos de outras funções
"""

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

# v = saudacao('Bom dia')
# print(v)
def executa(funcao, *args):
    return funcao(*args)

print(executa(saudacao, 'Bom dia', 'Camila'))