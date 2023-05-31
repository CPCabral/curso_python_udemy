# entendendo os seu proprios módulos python
#o primeiro modulo executado chama-se __main__

print('Este módulo se chama', __name__)

#importar outro modulo ou parte
# só pode mportar se estiver na mesma pasta
import sys
import aula75
print('Este módulo se chama', __name__)
print(*sys.path, sep='\n')