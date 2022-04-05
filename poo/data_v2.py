class Data:
    def __init__(self, dia=1, mes=1, ano=1970):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    # Metodo mágico sempre que precisa converter para string é chamado
    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


# Instância do Objeto
d1 = Data(5, 11, 1998)
print(d1)

d2 = Data(8, 10, 2004)
print(d2)

d3 = Data()
print(d3)
