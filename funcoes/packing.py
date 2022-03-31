from pyrsistent import v


def soma_2(a, b):
    return a + b


def soma_3(a, b, c):
    return a+b+c


# Transforma em uma tupla de valores, semelhante ao rest em JS
def soma_n(*nums):
    soma = 0
    for n in nums:
        soma += n
    return soma


if __name__ == '__main__':
    print(soma_2(2, 3))
    print(soma_3(2, 4, 6))
    
    # Packing
    print(soma_n(1))
    print(soma_n(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    
    # Unpacking
    tupla_nums = (1, 2, 3)
    print(soma_3(*tupla_nums))
    lista_nums = [1, 2, 3]
    print(soma_3(*lista_nums))
