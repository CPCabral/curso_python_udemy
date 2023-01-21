nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
tamanho = len(nome)

if (nome == '') or (idade == ''):
    print("Desculpe, você deixou campos vazios.")
else:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[-1:-(tamanho+1):-1]}')
    if ' ' in nome :
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
    print(f'Seu nome tem {tamanho} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[tamanho-1]}')
    
if nome and idade:
    ...
else:
    print("Desculpe, você deixou campos vazios.")   