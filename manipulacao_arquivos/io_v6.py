# usando a palavra with garantimos que o recuso criado sera fechado ao final do bloco
with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:
        for linha in arquivo:
            pessoa = linha.strip().split(',')
            #Muda onde será escrita a saida do arquivo
            print('Nome: {} Idade: {}'.format(*pessoa), file = saida)

if arquivo.closed:
    print('Arquivo fechado!')
    
if saida.closed:
    print('Arquivo de saida fechado!')
