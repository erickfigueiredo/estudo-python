bloco_atrs = ('bloco_accesskey', 'bloco_id')
ul_atrs = ('ul_id', 'ul_id')


def filtrar_atrs(informados, suportados):
    # Lembrando que o -1 no indice captura o ultimo elemento do array
    return ' '.join(f'{inf.split("_")[-1]}="{v}"'
                    for inf, v in informados.items() if inf in suportados)


def tag_bloco(conteudo, *args, classe='success', inline=False, **novos_atrs):
    tag = 'span' if inline == True else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args, **novos_atrs)
    atributos = filtrar_atrs(novos_atrs, bloco_atrs)
    return f'<{tag} {atributos} class="{classe}">{html}</{tag}>'


def tag_lista(*items, **novos_atrs):
    # O parentesis mais interno é opcional
    lista = ''.join((f'<li>{item}</li>' for item in items))
    return f'<ul {filtrar_atrs(novos_atrs, ul_atrs)}>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('bloco e classe', classe='info', inline=True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco(inline=True, conteudo='inline'))
    print(tag_bloco('falhou', classe='error'))
    print(tag_bloco(tag_lista('Item 1', 'Item 2', 'Item 3'), 'info'))
    # Uma vez que packing é aplicado, após ele argumentos deve ser nomeados e não posicionais
    print(tag_bloco(tag_lista, 'Sábado', 'Domingo', classe='info', inline=True))
    print(tag_bloco(tag_lista, 'Item 1', 'Item 2', classe='info', bloco_accesskey='m',
                    bloco_id='conteudo', ul_id='lista'))
