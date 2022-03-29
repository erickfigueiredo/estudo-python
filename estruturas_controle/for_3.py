product = {'name': 'Caneta Chic', 'price': 12.99,
           'imported': True, 'inventory': 120}

for key in product:
    print(key)
    
for value in product.values():
    print(value)
    
for key, value in product.items():
    print(key + ' = ', value)

# após o for, os valores key e value estarão disponiveis para uso
# Seus valores serão do ultimo valor obtido após a iteração

print(key, value)