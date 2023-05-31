# introdução a generator functions em python
# generator = (n for n in range(1000))

def funcao(n=0):
    return 1

fun = funcao(n=0)
print(fun)

#generator função que pausa ao invés de parar
def generator(n=0):
    yield 1 #pausar
    print('continuando...')
    yield 2 #pausar
    print('mais uma vez')
    yield 3 #pausar
    print('vou terminar')
    return 'Acabou!'

gen = generator(n=0)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
for n in gen:
    print(n)


def generator1(n=0, maximun=10):
    while True:
        yield n
        n += 1

        if n >= maximun:
            return
  

gen1 = generator1()

for n in gen1:
    print(n)