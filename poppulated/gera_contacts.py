import csv
from comentarios.models import Comentario
from posts.models import Post


def csv_to_list(filename: str) -> list:
    with open(filename) as csv_file:
        reader = csv.DictReader(csv_file)
        csv_data = [line for line in reader]
    return csv_data


def save_data(data):
    '''
    Salva os dados no banco.
    '''
    aux = []
    for item in data:
        nome = item.get('nome')
        email = item.get('email')
        comentario = item.get('comentario')
        _post = int(item.get('post'))
        post = Post.objects.filter(id=_post).first()
        postado = bool(item.get('postado'))
        obj = Comentario(
            nome_comentario=nome,
            email_comentario=email,
            comentario=comentario,
            post_comentario=post,
            publicado_comentario=postado,
        )
        
        aux.append(obj)
    
    return aux


data = csv_to_list('poppulated/comments.csv')
list_obj = save_data(data)

Comentario.objects.bulk_create(list_obj)
