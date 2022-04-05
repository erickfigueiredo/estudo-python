from datetime import datetime as dt


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []
        
    def __iter__(self):
        return self.tarefas.__iter__()

    def add(self, desc):
        self.tarefas.append(Tarefa(desc))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        # Possível index error
        return [tarefa for tarefa in self.tarefas
                if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s))'


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = dt.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + (' (Concluido)' if self.feito else '')


if __name__ == '__main__':
    casa = Projeto('Tarefas de Casa')
    casa.add('Passar Roupa')
    casa.add('Lavar Prato')
    print(casa)

    casa.procurar('Lavar Prato').concluir()
    for tarefa in casa:
        print(f'- {tarefa}')
    print(casa)

    mercado = Projeto('Compras no mercado')
    mercado.add('Frutas secas')
    mercado.add('Carne')
    mercado.add('Tomate')
    print(mercado)

    comprar_carne = mercado.procurar('Carne')
    comprar_carne.concluir()
    print(mercado)
