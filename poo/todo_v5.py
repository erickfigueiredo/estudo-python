from datetime import datetime as dt, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    def add(self, desc, vencimento=None):
        self.tarefas.append(Tarefa(desc, vencimento))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        # Possível index error
        return [tarefa for tarefa in self.tarefas
                if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s))'


class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = dt.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
            status.append('(Concluido)')
        elif self.vencimento:
            if dt.now() > self.vencimento:
                status.append('(Vencida)')
        else:
            dias = (self.vencimento - dt.now()).days
            status.append(f'(Vence em {dias} dias)')

        return f'{self.descricao} ' + ' '.join(status)


class TarefaRecorrente(Tarefa):
    def __init__(self, desc, vencimento, dias=7):
        super().__init__(desc, vencimento)
        self.dias = dias

    def concluir(self):
        super().concluir()
        novo_vencimento = dt.now() + timedelta(days=self.dias)
        return TarefaRecorrente(self.desc, novo_vencimento, self.dias)


if __name__ == '__main__':
    casa = Projeto('Tarefas de Casa')
    casa.add('Passar Roupa', dt.now())
    casa.add('Lavar Prato', dt.now() + timedelta(days=3, minutes=12))
    casa.tarefas.append(TarefaRecorrente('Trocar lencois', dt.now(), 7))
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
