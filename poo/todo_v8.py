from datetime import datetime as dt, timedelta


class TarefaNaoEncontrada(Exception):
    pass


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    def _add_tarefa(self, tarefa, **kwargs):
        self.tarefas.append(tarefa)

    def _add_nova_tarefa(self, descricao, **kwargs):
        self.tarefas.append(Tarefa(descricao, kwargs.get('vencimento', None)))

    def add(self, tarefa, vencimento=None, **kwargs):
        func_escolhida = self._add_tarefa if isinstance(tarefa, Tarefa) \
            else self._add_nova_tarefa
        kwargs['vencimento'] = vencimento
        func_escolhida(tarefa, **kwargs)

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        try:
            return [tarefa for tarefa in self.tarefas
                    if tarefa.descricao == descricao][0]
        except IndexError as e:
            raise TarefaNaoEncontrada(str(e))

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
    def __init__(self, descricao, vencimento, dias=7):
        super().__init__(descricao, vencimento)
        self.dias = dias
        self.dono = None

    def concluir(self):
        super().concluir()
        novo_vencimento = dt.now() + timedelta(days=self.dias)
        nova_tarefa = TarefaRecorrente(
            self.descricao, novo_vencimento, self.dias)
        if self.dono:
            self.dono += nova_tarefa
        return nova_tarefa


if __name__ == '__main__':
    casa = Projeto('Tarefas de Casa')
    casa.add('Passar Roupa', dt.now())
    casa.add('Lavar Prato', dt.now() + timedelta(days=3, minutes=12))
    casa.tarefas.append(TarefaRecorrente('Trocar lencois', dt.now(), 7))
    print(casa)
    
    try:
        casa.procurar('Lavar prato - ERRO')
    except TarefaNaoEncontrada as e:
        print (f'Erro: \n\t{str(e)}')
    finally:
        print('Sempre sendo executado!')
        
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
