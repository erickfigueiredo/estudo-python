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


if __name__ == '__main__':
    jose = Humano('Jose')
    grokn = Humano('Grokn').das_cavernas()
    print(jose, grokn)
    print(grokn.das_cavernas() is None)
    print(jose, grokn)
