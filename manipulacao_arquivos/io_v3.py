arquivo = open('pessoas.csv')

for linha in arquivo:
    print('Nome: {} Idade: {}'.format(*linha.strip().split(',')))

arquivo.close()
