#Decorar = Adicionar/ Remover/ restringir / alterar
#são funções que decoram outras funções

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('vou te decorar1')
        for arg in args:
            e_string(arg)
        resultado = func(*args,**kwargs)
        print('Ok, agora vc foi decorada')
        return resultado
    return interna

def inverte_string(string):
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser string')

inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string_checando_parametro('123')
print(invertida)