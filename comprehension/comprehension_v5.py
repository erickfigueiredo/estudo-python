dicionario = {f'item {i}': i * 2 for i in range(10) if not i % 2}
print(dicionario)

for num, dobro in dicionario.items():
    print(f'{num} x 2 = {dobro}')
