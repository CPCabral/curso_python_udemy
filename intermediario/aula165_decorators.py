#Decorar = Adicionar/ Remover/ restringir / alterar
#são funções que decoram outras funções

def inverte_string(string):
    return string[::-1]

invertida = inverte_string('camila')
print(invertida)