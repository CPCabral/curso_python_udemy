# Repetições
# while (enquanto)
# Executa uma ação enquanto uma condição é verdadeira
# loop infinito -> quando o código não tem fim
# ctrl+c para interromper

condicao = True

while condicao:
    print(1)
    print(2)
    print(3)
    nome = input('Qual é o seu nome: ')

    if nome == 'sair':
        break

print('Acabou!')