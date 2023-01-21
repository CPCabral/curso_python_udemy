'''
Imprecisão de ponto flutuante
double-precision floating-point format IEEE 754
'''


numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)
print(round(numero_3,1))
print(f'{numero_3:.2f}')

import decimal
numero_4 = decimal.Decimal('0.1')
numero_5 = decimal.Decimal('0.7')
*_, digito_1, digito_2 = cpf
print(numero_6)