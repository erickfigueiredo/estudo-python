# 0, 1, 1, 2, 3, 5, 8, 13, 21...
def fibonacci(qtd):
    resultado = [0, 1]
    for _ in range(2, qtd):
        # Seleciona o penúltimo e o último
        resultado.append(sum(resultado[-2:]))

    return resultado


if __name__ == '__main__':
    #Informa a quantidade de números de fibonacci desejados
    res = fibonacci(20)
    for fib in res:
        print(fib)
        