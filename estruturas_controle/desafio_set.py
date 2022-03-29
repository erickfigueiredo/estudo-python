FORBIDDEN_WORDS = {'futebol', 'religiao', 'politica'}

texts = [
    'Joao gosta de futebol e politica',
    'A praia foi divertida'
]

for text in texts:
    intersec = FORBIDDEN_WORDS.intersection(set(text.lower().split()))
    if intersec:
        print('Texto possui palavras proibidas: ', intersec)
    else:
        print('Texto autorizado: ', text)
