# decoradores com parametros

def decoradora(func):
    print('Decoradora1')

    def aninhada(*args, **kwargs):
        print('aninhada')
        res = func(*args, **kwargs)
        return res
    return aninhada

@decoradora
def soma(x,y):
    return x + y

dez_mais_cinco = soma(10,5)