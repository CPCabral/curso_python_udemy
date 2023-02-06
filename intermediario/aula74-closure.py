def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}!'
    return saudar

s1 = criar_saudacao('Bom dia', 'Luiz')
s2 = criar_saudacao('Boa noite', 'Luiz')

print(s1())
print(s2())


def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


retornar_bom_dia = criar_saudacao('Bom dia')
retornar_boa_noite = criar_saudacao('Boa noite')

print(retornar_bom_dia('Camila'))
print(retornar_boa_noite('Camila'))