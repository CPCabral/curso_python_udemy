pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Vale',
}

dados_pessoa = {
    'idade': 18,
    'altura': 1.6,
}

pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa)
a,b = pessoa
print(a,b)
a,b = pessoa.values()
print(a,b)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('Não Nomeados: ', args)

    for chave, valor in kwargs.items():
        print(chave,valor)

mostro_argumentos_nomeados(1, 2, nome = 'Joana', qqr = 123)
mostro_argumentos_nomeados(**pessoa_completa)