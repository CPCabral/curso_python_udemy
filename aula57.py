'''
Lista de lista e seus índices
iterável dentro de outro iterável
'''
salas = [
    # 0         1
    ['Maria', 'Helena'], # 0
    # 0
    ['Elaine',], # 1
    # 0         1        2
    ['Luiz', 'João', 'Eduarda',(0,20,30,49,50)], # 2
]

# print(salas)
# print(salas[1])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][2])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)