def dobro(x):
    return x * 2


def quadrado(x):
    return x**2


if __name__ == '__main__':
    funcs = [dobro, quadrado] * 5
    
    for fun, numero in zip(funcs, range(1,11)):
        print(f'{fun.__name__} de {numero} eh {fun(numero)}')
        