'''
valores padrão para parâmetros
Ao definir uma função, os parâmetros podem ter valores padrão. Caso o valor não seja enviado para o parâmetro, o valor padrão será usado.
Refatorar: editar o seu código.
'''

def soma(x, y, z=0): # z=0 é um falsy
    if z:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)

soma(1, 2)
soma(3, 5)
soma(7, 9, 0)
soma(1, 2, 3)


def soma(x, y, z=None): # todo parametro enviado apos um com valor padrão deve ter valor padrão também
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)

soma(1, 2)
soma(3, 5)
soma(7, 9, 0)
soma(1, 2, 3)

