from functools import reduce
from operator import add


# Garante imutabilidade
valores = (30, 10, 25, 70, 100, 94)

print(sorted(valores), valores)
print(min(valores))
print(max(valores))
print(sum(valores))
print(reduce(add, valores))
print(tuple(reversed(valores)))
