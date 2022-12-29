"""
Operadores lógicos
and (e) / or (ou) / not (não)

or - Qualquer condição verdadeira avalia toda a expressão como verdadeira

Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor

São considerados falsy:
0 0.0 '' False

também existe o tipo None que é usado para representar um não valor (NaN)
"""
entrada = 'e' #input('[E]ntrar [S]air: ')
senha_digitada = '123456' #input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

print(True or True)
print(True or False or 0 or 'abc')#Avaliação de curto circuito
print(0 or False or 0 or 'abc' or True)#Avaliação de curto circuito
print(True or 0 or True)
print(0.0 or 0 or False)

senha = input('Senha: ') or 'Sem senha'
print(senha)

 