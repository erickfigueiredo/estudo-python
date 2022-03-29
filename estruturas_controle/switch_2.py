def get_day_type(d):
    days = {
        1: 'Weekend',
        2: 'Weekday',
        3: 'Weekday',
        4: 'Weekday',
        5: 'Weekday',
        6: 'Weekday',
        7: 'Weekend'
    }
    return days.get(d, '** invalid **')

if __name__ == '__main__':
    for d in range(8):
        print(f'{d}: {get_day_type(d)}')
