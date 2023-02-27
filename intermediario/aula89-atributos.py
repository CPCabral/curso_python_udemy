# dir, hasattr e getattr
# hasattr -> checa se tem atributo

string = 'Luiz'

if hasattr(string, 'upper'):
    print('Existe upper')
    print(string.upper())


string = 'Luiz'
metodo = 'upper'

if hasattr(string, metodo):
    print(f'Existe {metodo}')
    print(getattr(string, metodo)())
else:
    print('não existe o método', metodo)
