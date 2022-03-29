try:
    arquivo = open('pessoas.csv')

    for linha in arquivo:
        print('Nome: {} Idade: {}'.format(*linha.strip().split(',')))
except IndexError:
    # A palavra reservada pass, permite que um bloco vazio seja declarado
    pass
finally:
    arquivo.close()

if arquivo.closed:
    print('Arquivo fechado!')
    