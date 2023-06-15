# exercicio de adiar função
def soma(x,y):
    return x + y

def multiplica(x,y):
    return x * y

def criar_funcao(funcao,x):
    def interna(y):
        return funcao(x,y)
    return interna

soma5 = criar_funcao(soma,5)
multiplica10 = criar_funcao(multiplica,10)

print(soma5(10))
print(multiplica10(9))