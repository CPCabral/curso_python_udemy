# Exercício
# Crie funções que duplicam, triplicam e quadruplicam o numero recebido como parâmetro

numero = int(input('Insira um numero: '))
multiplicador = int(input('Quantas vezes deseja multiplicar o numero: '))

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

operacao = criar_multiplicador(multiplicador)

print(f'{numero} x {multiplicador} = {operacao(numero)}')