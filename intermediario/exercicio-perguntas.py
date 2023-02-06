# Exercício - Sistema de Perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '2', '3', '4'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '35', '10', '55'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/5?',
        'Opções': ['4', '3', '2', '1'],
        'Resposta': '2',
    },
]

acertos = 0

for bloco in perguntas:
    print('Pergunta:', bloco['Pergunta'])

    for i, opcao in enumerate(bloco['Opções']):
        print(f'{i}) {opcao}')
        i += 1
    escolha = int(input('Escolha a opção: '))
    
    if bloco['Opções'][escolha] == bloco['Resposta']:
        print(f'Você acertou! 🎉\n')
        acertos += 1
    else:
        print(f'Você errou! 💔\n')

print(f'Você acertou {acertos} de {len(perguntas)} perguntas')
