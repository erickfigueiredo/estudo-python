import csv

with open('pessoas.csv') as entrada:
    for p in csv.reader(entrada):
        print('Nome: {}, Idade: {}'.format(*p))
