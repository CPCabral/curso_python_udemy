#introdução f-strings
nome = 'Camila'
altura = 1.65
peso = 87
imc = peso/(altura**2)

linha = f'{nome} tem {altura:.2f}m de altura, pesa {peso} quilos e seu IMC é {imc:.2f}'
print (linha)
print(nome, 'tem', altura, 'm de altura,', 'pesa', peso, 'quilos e seu IMC é', imc)