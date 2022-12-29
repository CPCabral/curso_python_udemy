#if / elif      / else
#se / se não se / se não
entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema!')
elif entrada == 'sair':
    print('Você saiu do sistema!')
else:
    print('Entrada inválida!')


condicao = False

if condicao:
    print("Este é o código do if")
else:
    print('esta é o else do if')


if 10 ==10:
    print('outro if')

condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = False

if condicao1:
    print('código para condição 1')
elif condicao2:
    print('código para condição 2')
elif condicao3:
    print('código para condição 3')
elif condicao4:
    print('código para condição 4')
else:
    print('nenhuma condição atendida')