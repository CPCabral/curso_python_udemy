texto = 'Python'

for letra in texto:
    print(letra)
###
novo_texto = ''
for letra2 in texto:
    novo_texto += f'*{letra2}'
print(novo_texto + '*')