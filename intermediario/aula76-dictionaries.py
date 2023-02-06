pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}

# print(pessoa['nome'])

# for chave in pessoa:
#     print(chave, pessoa[chave])

pessoa = {}
chave = 'nome'

pessoa[chave] = 'Camila'
pessoa['sobrenome'] = 'Cabral'

print(pessoa)
print(pessoa[chave])

del pessoa['sobrenome']
print(pessoa)

print(pessoa.get('sobrenome', 'Não existe')) #padrão retorna None

if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])