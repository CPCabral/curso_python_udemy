"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um número inteiro: ')

try:
    numero_inteiro = int(numero)
    if numero_inteiro % 2 == 0:
        print(f'O número {numero} é par')
    else:
        print(f'O número {numero} é ímpar')
except:
    print('Não é um número inteiro')


#resolução:
entrada = input('Digite um número inteiro: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    ...
else:
    print('você não digitou um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('informe a hora: ')

try:
    hora_int = int(hora)
    if hora_int >= 0 and hora_int <= 11:
        print('Bom dia!')
    elif hora_int >= 12 and hora_int <= 17:
        print('Boa tarde')
    elif hora_int >= 18 and hora <= 23:
        print('Boa noite!')
    else:
        print('Não é uma hora válida!')
except:
    print('Não é uma hora válida!')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Insira seu primeiro nome: ')

try:
    numero = float(nome)
    print('Não é uma entrada válida!')
except:
    tamanho = len(nome)
    if tamanho <= 4:
        print('Seu nome é curto.')
    elif tamanho > 6:
        print('Seu nome é muito grande!')
    else:
        print('Seu nome é normal!')

