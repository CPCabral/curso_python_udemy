#verificar se digitou apenas um caractere
#verificar se é str
#verificar se letra está em palavra
#trocar letra em palavra
'''Randomizar palavras
from random import choice
 
palavras = ['uva', 'banana', 'perfume']
 
palavra = choice(palavras)
print(palavra)

import os

os.system('cls') #limpa o terminal
'''


palavra_secreta =  'perfume'
tamanho = len(palavra_secreta)
palavra_descoberta = tamanho * '*'
letras_digitadas = ''
contador = 0

while True:
    
    letra = input('Digite uma letra: ')
    contador += 1

    eletra = letra.isalpha()

    if eletra == False or len(letra) !=1:
        print('Não é um caractere válido')
        continue

    if letra in letras_digitadas:
        print('Você já tentou essa letra, tente outra! ')
        continue
    
    letras_digitadas += letra
    
    if letra in palavra_secreta:
        i = 0
        for teste in palavra_secreta:            
            if letra == teste:
                palavra_descoberta = palavra_descoberta[:i] + letra + palavra_descoberta[i+1:]
            i += 1
                
    else:
        print('não tem essa letra na palavra secreta, tente de novo')
    
    print('Palavra secreta: ', palavra_descoberta)

    if '*' not in palavra_descoberta:        
        print(f'A palavra secreta "{palavra_secreta}" foi encontrada com {contador} tentativas!')
        break

"""
forma melhor de montar palavra

if letra_digitada in palavra_secreta:
    letras_acertadas += letra_digitada

palavra_formada = ''
for letra_secreta in palavra_secreta:
    if letra_secreta in letras_acertadas:
         palavra_formada += letra_secreta
    else:
        palavra_formada += '*'   
"""