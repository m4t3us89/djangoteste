from django import forms
from .models import Cliente
from django.core.validators import MinLengthValidator
import re

class SearchClienteForm(forms.Form):
    query = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Palavra-Chave',
            'autofocus': True,
        }
    ))


class ClienteForm(forms.ModelForm):
    nome = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Seu nome'
        }
    ))
    idade = forms.IntegerField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Idade',
            'type':'number'
        }
    ))
    email = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        }
    )) 
    cpf = forms.CharField(label='', required=True, validators=[MinLengthValidator(11)], widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'CPF',
            #'type':'number'
        }
    ))   

    class Meta: #CLASSE Q PREENCHE O FORM
        model = Cliente
        fields = ['nome', 'idade', 'cpf', 'email']

    def clean(self):
         #raise forms.ValidationError('O nome não pode ser teste.')
        cleaned_data = super().clean()
        nome = cleaned_data.get("nome")
        idade = cleaned_data.get("idade")
        email = cleaned_data.get('email')
        if 'teste' in nome:
            self.add_error('nome', 'O nome não pode ser teste.')
        if idade < 18:
            self.add_error('idade', 'A idade deve ser maior de 18 anos.') 
        if bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email)) == False:
            self.add_error('email', 'Por favor, digite um e-mail correto.')        


    




