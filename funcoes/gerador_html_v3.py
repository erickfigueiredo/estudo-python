def tag_bloco(conteudo, classe='success', inline=False):
    tag = 'span' if inline == True else 'div'
    return f'<{tag} class="{classe}">{conteudo}</{tag}>'


def tag_lista(*items):
    # O parentesis mais interno é opcional
    lista = ''.join((f'<li>{item}</li>' for item in items))
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('bloco e classe', 'info', True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco(inline=True, conteudo='inline'))
    print(tag_bloco('falhou', classe='error'))
    print(tag_bloco(tag_lista('Item 1', 'Item 2', 'Item 3'), 'info'))
