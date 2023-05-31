#funções que sabem pausar
import sys

generator = (n for n in range(1000))

print(generator)
print(sys.getsizeof(generator))

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

for n in generator:
    print(n)