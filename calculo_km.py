print('cálculo km rodados')
# jan = input('kms rodados em janeiro: ')
# fev = input('kms rodados em fevereiro: ')
# mar = input('kms rodados em março: ')
# abr = input('kms rodados em abril: ')
# mai = input('kms rodados em maio: ')
# jun = input('kms rodados em junho: ')
# jul = input('kms rodados em julho: ')
# ago = input('kms rodados em agosto: ')
# set = input('kms rodados em setembro: ')
# out = input('kms rodados em outubro: ')
# nov = input('kms rodados em novembro: ')
# dez = input('kms rodados em dezembro: ')

meses = ['janeiro','fevereiro','março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
soma = 0
contador = -1
for i in meses:
    contador = contador+1
    soma=soma+float(input(f'kms rodados em {meses[contador]}: '))

print(f'Foram rodados {soma}kms neste ano!')