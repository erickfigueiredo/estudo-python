lista_1 = [1, 2, 3]
dobro  = map(lambda x: x * 2, lista_1)
print(list(dobro))

lista_2 = [
    {'nome': 'Joao', 'idade': 32},
    {'nome': 'Maria', 'idade': 27},
    {'nome': 'Jose', 'idade': 18},
]
so_nomes = map(lambda d: d['nome'], lista_2)
print(tuple(so_nomes))
