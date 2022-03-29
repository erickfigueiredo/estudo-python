def faixa_etaria(idade):
    if 0 <= idade < 18:
        return 'Menor de Idade'
    elif idade in range(18, 64):
        return 'Adulto'
    elif idade in range(64, 100):
        return 'Melhor idade'
    elif idade >= 100:
        return 'Centenario'
    else:
        return 'idade invalida'


if __name__ == '__main__':
    for idade in (18, 35, 87, 113, -2, 100, 64, 99):
        print(f'{idade}: {faixa_etaria(idade)}')
