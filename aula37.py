
contador = 0 
while contador <= 100:
    contador += 1
    
    if contador >= 6 and contador <= 10:
        continue # pula esse passo

    print (contador)

    if contador == 15:
        break # quebra o laço

print('acabou!')
