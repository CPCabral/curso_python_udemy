# iterando strings com while

nome = 'Luiz Otávio'
tamanho = len(nome)
posicao_letra = 0
novo_nome = ''

while posicao_letra < tamanho:
    letra = nome[posicao_letra]
    print(letra)
    novo_nome += f'*{letra}'
    posicao_letra += 1

novo_nome += '*'
print(novo_nome)