FORBIDDEN_WORDS = ('futebol', 'religiao', 'politica')

texts = [
    'Joao gosta de futebol e politica',
    'A praia foi divertida'
]

for text in texts:
    found = False
    for word in text.lower().split():
        if word in FORBIDDEN_WORDS:
            print('O texto possui pelo menos uma palavra proibida', word)
            found = True
            break
        
    if not found:
        print('Texto autorizado: ', text)
