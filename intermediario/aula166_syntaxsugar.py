# @syntax_sugar - açucar sintático

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('vou te decorar!')
        for arg in args:
            e_string(arg)
        resultado = func(*args,**kwargs)
        print('Ok, agora vc foi decorada')
        return resultado
    return interna

@criar_funcao
def inverte_string(string):
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser string')


invertida = inverte_string('123')
print(invertida)