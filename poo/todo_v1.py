from datetime import datetime as dt

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
    casa = []
    casa.append(Tarefa('Passar roupa'))
    casa.append(Tarefa('Lavar prato'))
    
    [tarefa.concluir() for tarefa in casa if tarefa.descricao == 'Lavar prato']
    for tarefa in casa:
        print(f'- {tarefa}')
    