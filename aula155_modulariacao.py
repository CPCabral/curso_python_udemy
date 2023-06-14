import importlib
#from aula155_m import variavel_modulo
import aula155_m

for i in range(1,10):
    print(i)
    importlib.reload(aula155_m)

