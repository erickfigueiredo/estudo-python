class Carro:
    def __init__(self, limite=0):
        self.limite = limite
        self.velocidade = 0

    def acelerar(self, delta=5):
        if self.velocidade + delta <= self.limite:
            self.velocidade += delta
        elif self.limite - self.velocidade > 0:
            self.velocidade += self.limite - self.velocidade
        return self.velocidade 

    def frear(self, delta=5):
        if self.velocidade - delta > 0:
            self.velocidade -= delta
        else:
            self.velocidade = 0
        return self.velocidade 


if __name__ == '__main__':
    c1 = Carro(180)

    for _ in range(25):
        print(c1.acelerar(8))

    for _ in range(10):
        print(c1.frear(delta=20))
