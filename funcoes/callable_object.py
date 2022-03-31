class Potencia:
    # Calcula a potência de alfum numero
    def __init__(self, expoente):
        self.expoente = expoente

    def __call__(self, base):
        return base ** self.expoente


if __name__ == '__main__':
    quadrado = Potencia(2)
    cubo = Potencia(3)

    if callable(quadrado) and callable(cubo):
        print(f'9^2 = {quadrado(9)}')
        print(f'6^3 = {cubo(6)}')
        print(f'8^4 = {Potencia(4)(8)}')
