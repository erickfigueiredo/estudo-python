def multiplicar(x):
    # Calcular tem consciencia do seu escopo
    # Com isso ela sabe o valor de x (definido em seu contexto)
    def calcular(y): 
        return x * y
    return calcular # Lazy evaluation


if __name__ == '__main__':
    dobro = multiplicar(2)
    triplo = multiplicar(3)
    print(dobro, triplo)
    print(f'O triplo de 3 eh {triplo(3)}')
    print(f'O dobro de 7 eh {dobro(7)}')