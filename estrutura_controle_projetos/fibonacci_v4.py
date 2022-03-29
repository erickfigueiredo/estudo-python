# 0, 1, 1, 2, 3, 5, 8, 13, 21...
def fibonacci(limite):
    resultado = [0, 1]
    while resultado[-1] < limite:
        # Seleciona o penúltimo e o último
        resultado.append(sum(resultado[-2:]))

    return resultado


if __name__ == '__main__':
    res = fibonacci(100)
    for fib in res:
        print(fib)