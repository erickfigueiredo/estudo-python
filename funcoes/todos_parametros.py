def todos_params(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')


if __name__ == '__main__':
    # Parametros posicionais
    todos_params('a', 'b', 'c')
    # Parametros nomeados
    todos_params(nome='Erick', idade='secret')
    todos_params(1, 2, 3, legal=True, valor=12.99)
    todos_params('Ana', False, [1, 2, 3], tamanho='M', fragil=False)
    # todos_params(primeiro='Joao', 'Maria') Erro (posicional devem vir antes)
