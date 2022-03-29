import sys
from math import pi


def calc(r):
    return pi * float(r)**2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'É necessário informar o raio do círculo.\nSintaxe: {sys.argv[0]} <raio>')
    else:
        raio = sys.argv[1]
        area = calc(raio)
        print('Área do círculo', area)
        