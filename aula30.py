'''
CONSTANTE = "variáveis" que não vão mudar (caixa alta)
muitas condições no mesmo if (ruim)
    <- contagem de complexidade (ruim)
'''

velocidade = 61 #velocidade atual do carro
local_carro = 100 #local que o carro está na estrada

RADAR_1 = 60 #velocidade máxima do radar 1
LOCAL_1 = 100 #local onde o radar 1 está
RADAR_RANGE = 1 #a distância ode o radar pega

vel_carro_passou_radar_1 = velocidade > RADAR_1
carro_multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) and vel_carro_passou_radar_1

if vel_carro_passou_radar_1:
    print('Velocidade carro passou do radar 1')

if carro_multado_radar_1:
    print('Carro multado em radar 1')