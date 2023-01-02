frase = 'O Python é uma linguagem de programação multiparadigma.'\
    'Python foi criado por Guido van Rossum.'

print(frase.count('Python'))

# a é diferente de á

#ver qual letra apareceu mais vezes
i = 0
qnt_apareceu_mais_vezes = 0
letra_que_apareceu_mais = ''

while i < len(frase):
    letra_atual = frase[i]
    i += 1

    if letra_atual == ' ':
        continue

    qnt_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qnt_apareceu_mais_vezes < qnt_apareceu_mais_vezes_atual:
        qnt_apareceu_mais_vezes = qnt_apareceu_mais_vezes_atual
        letra_que_apareceu_mais = letra_atual

    #print(letra_atual, qnt_apareceu_mais_vezes_atual)
    

print(f'A letra que apareceu mais vezes foi "{letra_que_apareceu_mais}" que apareceu {qnt_apareceu_mais_vezes}x')