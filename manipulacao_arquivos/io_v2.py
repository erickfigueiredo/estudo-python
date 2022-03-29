arquivo = open('pessoas.csv')

for linha in arquivo:
    print('Nome: {} Idade: {}'.format(*linha.split(',')))

arquivo.close()
