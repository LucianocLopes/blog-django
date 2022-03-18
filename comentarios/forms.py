from django.forms import ModelForm
import requests
from . import models


class FormComentario(ModelForm):
    
    def clean(self):
        raw_data = self.data
        recaptcha_reponse = raw_data.get('g-recaptcha-response')
        recaptcha_request = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data={
                'secret': '6LfxZuweAAAAAHxKYtifG6wGWU5ttx3Y5HE7cIdj',
                'response': recaptcha_reponse
            }
        )
        recaptcha_result = recaptcha_request.json()
        if not recaptcha_result.get('success'):
            self.add_error(
                'comentario',
                'Favor assinalar o campo "Não sou um robô"',
            )

        data = self.cleaned_data

        nome = data.get('nome_comentario')
        email = data.get('email_comentario')
        comentario = data.get('comentario')

        if len(nome) < 5:
            self.add_error(
                'nome_comentario',
                'Nome precisa ter mais de 5 caracteres!'
            )

    
    class Meta:
        model = models.Comentario
        fields = ('nome_comentario', 'email_comentario', 'comentario')
