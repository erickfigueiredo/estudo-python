def get_concept(g):
    grade = float(g)
    
    if grade > 9 and grade <= 10:
        return 'A'
    elif grade > 8:
        return 'A-'
    elif grade > 7:
        return 'B'
    elif grade > 6:
        return 'B-'
    elif grade > 5:
        return 'C'
    elif grade > 4:
        return 'C-'
    elif grade > 3:
        return 'D'
    elif grade > 2:
        return 'D-'
    elif grade > 1:
        return 'E'
    elif grade >= 0:
        return 'E-'
    else:
        return 'Nota inválida'


if __name__ == '__main__':
    grade = input('Nota do aluno: ')
    print('Conceito: ', get_concept(grade))