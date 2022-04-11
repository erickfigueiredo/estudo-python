from func_primeira_classe import dobro, quadrado

def processar(titulo, lista, func):
    print(f'Processando: {titulo}')
    for i in lista:
        print(i, '=>', func(i))
        
        
if __name__ == '__main__':
    processar('Dobros de 1 a 10', range(1, 11), dobro)
    processar('Quadrados de 1 a 10', range(1, 11), quadrado)
    