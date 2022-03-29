# 0, 1, 1, 2, 3, 5, 8, 13, 21...
def fibonacci(quantidade, sequencia=(0, 1)):
    return sequencia if len(sequencia) == quantidade else \
        fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))


if __name__ == '__main__':
    # Lista os n primeiros numeros da sequencia de
    for fib in fibonacci(20):
        print(fib)
