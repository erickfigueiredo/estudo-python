from math import pi

def calc(r):
    print(f'Area da Circunferencia: {pi * float(radius)**2}')

if (__name__ == '__main__'):
    radius = input('Informe o raio: ')
    calc(radius)
