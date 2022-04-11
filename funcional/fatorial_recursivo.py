def fatorial(n):
    if n == 1: return 1 
    return n * fatorial(n-1)


if __name__ == '__main__':
    print(f'10! = {fatorial(10)}')
    # 6 semanas em segundos == 10!
    print(6 * 7 * 24 * 60 * 60)
    