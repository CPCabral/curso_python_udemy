# PYTHON

### Comentários em Python
~~~py
# comentário de linha

"""
doc string
"comentário" de parágrafo (o interpretador lê)
"""

'''
doc string 
usar para escrever notas
'''
~~~

## Print

~~~py
print('argumento',12, sep="-", end='##\n')
print(34,12, sep='-', end = '##') # sep = separador
print(34,12, sep='-') # sep = separador

# Aspas duplas
print("Luiz Otávio")
print(2, "Luiz 'Otávio'")

# Escape
print("Luiz \"Otávio\"")

# r
print(r"Luiz \"Otávio\"")

# introdução f-strings
nome = 'Camila'
altura = 1.65
peso = 87
imc = peso/(altura**2)

linha = f'{nome} tem {altura:.2f}m de altura, pesa {peso} quilos e seu IMC é {imc:.2f}'
print (linha)
print(nome, 'tem', altura, 'm de altura,', 'pesa', peso, 'quilos e seu IMC é', imc)
~~~
### Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(caractere)(><^)(quantidade)
\> - Esquerda
< - Direita
^ - Centro
Sinal - + ou-
Ex.: 0>100,.1f
Conversion flags = !r !s !a
"""

variavel = 'ABCD'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.384270468:.1f}')
print(f'{1000.384270468:+.1f}')
print(f'{1000.384270468:0=+10,.1f}')
print(f'{-1000.384270468:.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
"""
nome = 'Luiz'
preco = 1000.95897643
variavel = 'Luiz, o preço total foi de R$ 1000.96'
variavel1 = '%s, o preço total foi de R$ %.2f' % (nome, preco)
print(variavel)
print(variavel1)

print('O hexadecimal de %d é %X' % (1500,1500))

## Operadores matemáticos

~~~py
adicao = 10 + 10
print("Adição: 10 + 10 = ", adicao)

subtracao = 10 - 5
print("Subtração: 10 - 5 = ", subtracao)

divisao = 10 / 3 #float
print("Divisão: 10 / 3 =", divisao)

divisao_truncada = 10 // 3
print("Divisão Truncada: 10 // 3 =", divisao_truncada)

exponenciacao = 2 ** 10
print("Exponenciação: 2 ** 10 = ", exponenciacao)

resto = 55 % 2
print('Resto: 55 % 2 = ', resto)

# precedencia de operadores
# 1. (n + n)
# 2. * / // %
# 4. + -
~~~
## Booleans
Operadores lógicos
`and` (e) / `or` (ou) / `not` (não)

- `and` - todas as condições precisam ser verdadeiras
Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor

- `or` - Qualquer condição verdadeira avalia toda a expressão como verdadeira. 
Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor


- São considerados falsy:
`0 0.0 '' False`

- também existe o tipo `None` que é usado para representar um não valor

- Operadores `in` e `not in` (estar entre/ não estar entre)
~~~py
"""
Operadores de comparação (relacionais)
OP        Significado        Exemplo
>         maior              2 > 1
>=        maior ou igual     2 >= 1
<         menor              1 < 2
>=        menor ou igual     2 <= 2
==        igual              'a' == 'a'
!=        diferente          'a' != 'b'
"""
~~~

Fatiamento de strings
012345678
Olá mundo

Fatiamento [i:f:p] [::]

Obs.: a função len retorna a quantidade de itens da str
variavel = "Olá mundo"
print(variavel[-4])
print(variavel[4:])
print(variavel[4:7]) #INDICE final NÃO É INCLUÍDO 

"""
Introdução ao try/except
try -> tentar eecutar o código
except -> ocorreu algum erro ao tentar executar
"""
## Repetições
~~~py
# while (enquanto)
# Executa uma ação enquanto uma condição é verdadeira
# loop infinito -> quando o código não tem fim
# ctrl+c para interromper 
~~~

"""
Operadores de atribuição
= += -= *= /= //= **= %=
"""

break # quebra o laço  
continue # pula esse passo

"""
for + range
range -> range(start, stop, step)
"""

numeros = range(10) #passando que quer números de 0-10  
`# numeros = range(5,10) #de 5 - 10`
`# numeros = range(5,10,2) #de 5 - 10 pulando 2`

"""
for
iterável -> str, range, etc (` __iter__`)
iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue o seu iterador
"""
Listas em Python
tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
    append - adiciona o item ao final
    insert - adiciona um item na posição escolhida
    pop - remove do final ou do indice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - stende a lista
    + - concatena a lista
Create Read Update   Delete
Criar, ler, alterar, apagar = lista [i] (CRUD)
"""
```py
# string = 'ABCDE' # 5 caracteres (len)
# lista = [] # ''
# #          0    1          2         3    4
# lista1 = [123, True, 'Luiz otávio', 1.2, []]
# #print(bool([]))  # falsy
# lista1[-3] = 'Maria'

# print(lista1)

# lista = [10, 20, 30, 40]
# lista[2] = 300
# print(lista)
# del lista[2]
# print(lista)
# lista.append(50)
# lista.append(60)
# print(lista)
# lista.pop()
# print(lista)
# removido = lista.pop(3)
# print(lista, 'removido', removido)
```
## Introdução ao desempacotamento + Tuples

```py
nomes = ['Maria', 'Helena', 'Luiz']

# nome1, nome2, nome3 = nomes
# print(nome2)

nome1, *resto = nomes
```

"""
split e join com list e str
split - divide uma sting
join - une em uma string
"""
frase = 'olha só que, coisa interessante'
lista_palavras = frase.split(', ')
print(lista_palavras)

#.strip() corta espaços do começo e fim
"""

### Operação ternária (condicional de uma linha)

if else em uma linha  
>`<valor> if <condição> else <outro valor>`
```py
digito = 9
novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)

print('Valor' if True else 'Outro valor' if True else 'Fim')
```
## Funções

Introdução às funções (def) em Python  
Funções são trechos de códigos usados para replicar determinada ação ao longo do seu código.  
Elas podem receber valores para parâmetros (argumentos) e retornar um valor específico.
por padrão, funções Python retornam `None` (nada)
~~~py
def imprimir(a, b, c):
    print(a)
    print(b)
    print(c)

imprimir(1,2,3)
~~~
#### **Argumentos nomeados e não nomeados em funções Python**
- Argumento nomeado tem nome com sinal de igual
- Argumento não nomeado recebe apenas o argumento (valor)
```py
def soma(x,y):
    print(f'{x=} y={y}','|','x + y =', x + y)

soma(1,2) #argumento posicional, depende da ordem 1->x e 2-> y
soma(y=2,x=1) #argumento nomeado
soma(1,y=2) #se nomear um argumento os próximos tbm tem que ser nomeado
```
#### **Valores padrão para parâmetros**
Ao definir uma função, os parâmetros podem ter valores padrão. Caso o valor não seja enviado para o parâmetro, o valor padrão será usado.
~~~py
def soma(x, y, z=0): # z=0 é um falsy
~~~
#### **Escopo de funções em python**
Escopo significa um local onde aquele código pode atingir.  
Existe o escopo local e global.
- O escopo global é onde todo o código é alcançável
- O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.

>Tudo que  é definido dentro da função não pode ser alterado fora dela.  
~~~py
x = 10

def escopo():

    def outra_funcao():
        global x #mexendo no x  global (MÁ PRÁTICA)
        x = 11
        y = 3
        z = 2
        print(f'{x=},{y=}')

    outra_funcao()
    x = 1 #escopo local
    print(f'{x=},{y=}')


y = 2 #escopo global
print(f'{x=}')
escopo()
# print(z) erro, pois só está definido no escopo da função
print(f'{x=}')
~~~
#### **Return**
Retorno de valores das funções (return)  
>print -> não tem valor, função que exibe o valor de outro objeto

~~~py
def soma(x,y):
    return x + y #termina o código da função
    print(1+1) # código inalcansável
~~~

#### **Argumentos não nomeados**
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)

~~~py
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(x, y):
    return x + y

def soma(*args):
    total = 0
    for numero in args:
        total += numero
        
    return total

numeros = 1, 2, 3, 4, 5, 6

soma123 = soma(*numeros)
print(soma123)

print(sum(numeros)) #função de soma do python
~~~

#### Higher Order Functions

- Funções que podem receber e/ou retornar outras funções
- Passar funções como argumentos de outras funções

#### Funções de primeira classe

- First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

#### Closure
funções que retornam outras funções

## Dicionários em Python (tipo dict)
Dicionários são estruturas de dados do tipo "chave" e "valor".
- Chaves podem ser consideradas como o "índice" que vimos na lista e podem ser de tipos imutáveis
- O valor pode ser de qualquer tipo, inslusive outro dicionário
- usamos as chaves `{ }` ou a classe `dict` para criar dicionários
> Imutáveis: str, int, float, bool, tuple, etc.
> Mutáveis: dict, list

```py
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}
# print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['sobrenome'])

print()

for chave in pessoa:
    print(chave, pessoa[chave])
```
#### **Métodos úteis dos dicionários em Python**
`len` - quantas chaves
`keys` - iterável com as chaves
`values` - iterável com os valores
`items` - iterável com chaves e valores
`setdefault` - adiciona valor se a chave não existe
`copy` - retorna uma cópia rasa (shallow copy)
`get` - obtém uma chave
`pop` - Apaga um item com a chave especificada (del)
`popitem` - Apaga o último item adicionado
`update` - Atualiza um dicionário com outro

# Sets
Conjuntos em Python  
São mutáveis mas só aceitam tipos imutáveis como valor interno.

Criando um set:
>set(item1, item2, item3)
>{item1, item2, item3}
>set() set vazio

Sets são eficientes para remover valores duplicados de iteráveis
 - eles não tem indexes;
 - eles não garantesm ordem;
 - eles são iteráveis (for, in, not in)


Métodos úteis:
`add`, `update`, `clear`, `discard`

Operadores úteis:
- união | união (union) - une
- intersecção & (intersection) - Itens presentes em ambos
- diferença - Itens Presentes apenas no set da esquerda
- diferença simétrica ^ - IItens que não estão em ambos

```py
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2 # união
s4 = s1 & s2 # intersecção
s5 = s1 - s2 # diferença - itens disponíveis apenas no primeito set
s6 = s2 - s1 # diferença - itens disponíveis apenas no primeito set
s7 = s1 ^ s2 # diferença simétrica - itens não presentes em ambos s5 | s6
```

### Falsy
lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteiro = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)



#GIT

git init
git add .
git commit -m 'comentário'
git push