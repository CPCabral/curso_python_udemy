"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
argumento não nomeado recebe apenas o argumento (valor)
"""
def soma(x,y):
    print(f'{x=} y={y}','|','x + y =', x + y)

soma(1,2) #argumento posicional, depende da ordem 1->x e 2-> y
soma(y=2,x=1) #argumento nomeado
soma(1,y=2) #se nomear um argumento os próximos tbm tem que ser nomeado

