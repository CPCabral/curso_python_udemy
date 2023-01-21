"""
Operadores lógicos
and (e) / or (ou) / not (não)

and - todas as condições precisan ser verdadeiras

Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor

São considerados falsy:
0 0.0 '' False

também existe o tipo None que é usado para representar um não valor (NaN)
"""
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

print(True and True)
print(True and False and True)#Avaliação de curto circuito
print(True and 0 and True)
print(bool(''))
print(bool(0.0))
 