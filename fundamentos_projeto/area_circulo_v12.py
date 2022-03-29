import sys
import errno
from math import pi


class TerminalColor:
    ERROR = '\033[91'
    DEFAULT = '\033[0m'


def calc(r):
    return pi * float(r)**2


def help(program_name):
    print(
        f'É necessário informar o raio do círculo.\nSintaxe: {program_name} <raio>')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help(sys.argv[0])
        sys.exit(errno.EPERM)
    # elif
    if not sys.argv[1].isnumeric():
        help(sys.argv[0])
        print(TerminalColor.ERROR +
              'O raio deve ser um valor numerico!' + TerminalColor.DEFAULT)

        sys.exit(errno.EINVAL)

    raio = sys.argv[1]
    area = calc(raio)
    print('Área do círculo', area)
