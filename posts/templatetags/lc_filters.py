from django import template


register = template.Library()


@register.filter(name='plural_comentarios')
def plural_comentarios(num_comentarios: int) -> str:
    try:
        nums = int(num_comentarios)
        match nums:
            case 0:
                return f'Nenhum comentário'
            case 1:
                return f'{nums} comentário'
            case _:
                return f'{nums} comentários'
    except:
        return f'{num_comentarios} comentário(s)'
