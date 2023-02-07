# isinstance - para saber se dado é de determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1,2), {0, 1},
    {'nome': 'Camila'},
]

for item in lista:
    print(item, isinstance(item, set))

    if isinstance(item, (int, float)):
        print(item, item*2)