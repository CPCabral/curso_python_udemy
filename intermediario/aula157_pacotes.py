# módulo é um arquivo
# package é uma pasta

# criar aquivo na raiz para ser o __main__, a partir desse arquivo cria as outras coisas que serão chamadas

print(__name__)
# opção 1 (melhor)
from aula157package.modulo import soma_do_modulo

print(soma_do_modulo(10,48))

# opção 2
import aula157package.modulo
print(aula157package.modulo.soma_do_modulo(1,3))

# opção 3
from aula157package import modulo
print(modulo.soma_do_modulo(1,5))

#opção 4 

from aula157package.modulo2 import * #* significa "all"

print(variavel)
print(soma_do_modulo(1,5))
