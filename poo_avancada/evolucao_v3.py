class Humano:
    # Atributo de Classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError('Idade deve ser um número positivo!')
        self._idade = idade

    def das_cavernas(self):
        # Esse pertence a instância
        # Se na instância houver o atributo, então há prioridade
        self.especie = 'Homo Neanderthalensis'
        return self

    def __str__(self):
        return f'Nome: {self.nome} Idade: {self.get_idade()} Especie: {self.especie}\n'

    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis',
                     'Sapiens')
        return ('Australopiteco',)+tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod
    def e_evoluido(cls):
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):
    especie = Humano.especies()[-2]


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == '__main__':
    jose = HomoSapiens('Jose')
    # Acessamos como se fosse um atributo graças ao Decorator
    jose.idade = 40
    print(f'Nome: {jose.nome}, Idade: {jose.idade}')
