arquivo = open('pessoas.csv')
dados = arquivo.read()
arquivo.close()

for linha in dados.splitlines():
    print('nome: {}, idade: {}'.format(*linha.split(',')))
