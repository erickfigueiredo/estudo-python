class Humano:
    # Atributo de Classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        # Esse pertence a instância
        # Se na instância houver o atributo, então há prioridade
        self.especie = 'Homo Neanderthalensis'
        return self
        
    def __str__(self):
        return f'Nome: {self.nome} Especie: {self.especie}\n'
    
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
    grokn = Neanderthal('Grokn').das_cavernas()
    print(grokn)
    print(f'Evolucao (a partir da classe): {", ".join(HomoSapiens.especies())}')
    print(f'Evolucao (a partir da instancia): {", ".join(jose.especies())}')
    print(f'Homo Sapiens Evoluido? {"Sim" if HomoSapiens.e_evoluido() else "Nao"}')
    print(f'Neanderthal Evoluido? {"Sim" if Neanderthal.e_evoluido() else "Nao"}')
    print(f'Jose Evoluido? {"Sim" if jose.e_evoluido() else "Nao"}')
    print(f'Grokn Evoluido? {"Sim" if grokn.e_evoluido() else "Nao"}')
    