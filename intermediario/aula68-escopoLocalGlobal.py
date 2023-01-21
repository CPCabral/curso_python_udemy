'''
Escopo de funções em python 
Escopo significa um local onde aquele código pode atingir.
Existe o escopo local e global.
O escopo global é onde todo o código é alcançável
o escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.

Tudo que  é definido dentro da função não pode ser alterado fora dela
'''
x = 10

def escopo():

    def outra_funcao():
        global x #mexendo no x  global (MÁ PRÁTICA)
        x = 11
        y = 3
        print(f'{x=},{y=}')

    outra_funcao()
    x = 1 #escopo local
    print(f'{x=},{y=}')


y = 2 #escopo global
print(f'{x=}')
escopo()
# print(x) erro, pois só está definido no escopo da função
print(f'{x=}')