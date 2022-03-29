# Gerador de numeros sob demanda que consome menos memória que a comprehension
generator = (i ** 2 for i in range(10) if not i%2)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
# print(next(generator)) Resulta em erro!
