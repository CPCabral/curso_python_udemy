# Calculadora com while

while True:
    numero_1 = input('digite um número: ')
    numero_2 = input('digite outro: ')
    operador = input('digite o operador (+-/*): ')

    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
        
        if numeros_validos is None:
            print('Um ou ambos os números digitados são inválidos.')
            continue
    
    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('digite apenas um operador.')
        continue

    ###

    if operador == '+':
        print(f'O resultado da soma entre {num_1_float} e {num_2_float} é ',num_1_float + num_2_float)
    elif operador == '-':
        print(f'O resultado da subtração entre {num_1_float} e {num_2_float} é ',num_1_float - num_2_float)
    elif operador == '*':
        print(f'O resultado da multiplicação entre {num_1_float} e {num_2_float} é ', num_1_float * num_2_float)
    elif operador == '/':
        print(f'O resultado da subtração entre {num_1_float} e {num_2_float} é ', num_1_float / num_2_float)


    # sair = input('Quer [s]air: ')
    # sair = sair.lower()
    # sair = sair.startswith('s')
    sair = input('Quer [s]air: ').lower().startswith('s')
    print(sair)

    if sair is True:
        break