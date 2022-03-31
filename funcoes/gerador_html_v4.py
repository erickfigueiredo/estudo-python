def tag_bloco(conteudo, *args, classe='success', inline=False):
    tag = 'span' if inline == True else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args)
    return f'<{tag} class="{classe}">{html}</{tag}>'


def tag_lista(*items):
    # O parentesis mais interno é opcional
    lista = ''.join((f'<li>{item}</li>' for item in items))
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('bloco e classe', classe='info', inline=True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco(inline=True, conteudo='inline'))
    print(tag_bloco('falhou', classe='error'))
    print(tag_bloco(tag_lista('Item 1', 'Item 2', 'Item 3'), 'info'))
    # Uma vez que packing é aplicado, após ele argumentos deve ser nomeados e não posicionais
    print(tag_bloco(tag_lista, 'Sábado', 'Domingo', classe='info'))
