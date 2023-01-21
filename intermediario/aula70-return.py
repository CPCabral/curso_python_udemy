'''
Retorno de valores das funções (return)
print -> não tem valor, função que exibe um valor de outro objeto
'''

variavel = print('Luiz')
print(variavel)

variavel = int('1')

def soma(x,y):
    return x + y #termina o código da função
    print(1+1) # código inalcansável

soma1 = soma(2,2)
soma2 = soma(3,3)
print(soma1 + soma2)