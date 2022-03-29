import sys
from math import pi

def calc(r):
    return pi * float(r)**2

if (__name__ == '__main__'):
    # Assim como é feito no C++
    if len(sys.argv) > 1:
        radius = sys.argv[1]
    else:
        radius = input('Informe o raio: ')
    print(f'Area da circunferencia: {calc(radius)}')
