from django.db import models
from django.core.validators import MinLengthValidator
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    cpf = models.CharField(max_length=11, validators=[MinLengthValidator(11)])
    email = models.CharField(max_length=100, default='Não informado')
    #descricao = models.TextField()
    
    def __str__(self):#funcao parar retornar no painel administrador
        return self.nome 

