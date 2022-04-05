from abc import ABCMeta, abstractproperty


# Definindo uma classe abstrata
class Humano(metaclass=ABCMeta):
    # Atributo de Classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    @abstractproperty
    def inteligente(self):
        pass

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

    @property
    def inteligente(self):
        return False


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]

    @property
    def inteligente(self):
        return True


if __name__ == '__main__':

    try:
        anonimo = Humano('John Doe')
        print(anonimo.inteligente)
    except TypeError:
        print('Classe Abstrata')

    jose = HomoSapiens('José')
    print('{} da classe {}, inteligente {}'
        .format(jose.nome, jose.__class__.__name__, jose.inteligente))

    grong = Neanderthal('Grong')
    print('{} da classe {}, inteligente {}'
        .format(grong.nome, grong.__class__.__name__, grong.inteligente))
    