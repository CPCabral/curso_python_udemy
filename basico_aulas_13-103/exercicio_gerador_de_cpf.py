import random

nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0,9))

soma_digito_1 = 0
range_1 = 10
for numero in nove_digitos:
    soma_digito_1 += int(numero)*range_1
    range_1 -= 1

resto = (soma_digito_1*10) % 11

primeiro_digito = resto if resto <= 9 else 0

###Cálculo Digito 2###

dez_digitos = nove_digitos + str(primeiro_digito)
soma_digito_2 = 0
range_2 = 11
for numero in dez_digitos:
    soma_digito_2 += int(numero)*range_2
    range_2 -= 1

resto_2 = (soma_digito_2*10) % 11

segundo_digito = resto_2 if resto_2 <= 9 else 0

print(f'{nove_digitos[:3]}.{nove_digitos[3:6]}.{nove_digitos[6:]}-{str(primeiro_digito)+str(segundo_digito)}')