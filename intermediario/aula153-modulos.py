# import inteiro

import sys
platform = 'A minha'
# sys.exit() sai do programa
print(sys.platform) #plataforma que está usando

# partes

from sys import exit, platform
print(platform)

# importar com apelido
import sys as s
sys = 'alguma coisa'
print(s.platform)

# má pratica

from sys import * #importa tudo
print(platform)