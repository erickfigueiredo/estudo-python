# usando a palavra with garantimos que o recuso criado sera fechado ao final do bloco
with open('pessoas.csv') as arquivo:
    for linha in arquivo:
        print('Nome: {} Idade: {}'.format(*linha.strip().split(',')))

if arquivo.closed:
    print('Arquivo fechado!')
