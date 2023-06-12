# entendendo os seu proprios módulos python
#o primeiro modulo executado chama-se __main__

print('Este módulo se chama', __name__)

#importar outro modulo ou parte
# só pode mportar se estiver na mesma pasta
try:
    import sys
    sys.path.append('/Users/Camila/Desktop')
except:
    ...
import aula75
import teste
print('Este módulo se chama', __name__)
print(*sys.path, sep='\n')