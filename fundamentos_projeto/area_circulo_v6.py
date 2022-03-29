from math import pi

def calc(r):
    return pi * float(r)**2

if (__name__ == '__main__'):
    radius = input('Informe o raio: ')
    print(f'Area da circunferencia: {calc(radius)}')
