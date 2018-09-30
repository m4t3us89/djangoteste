from django.db import models
#python manage.py makemigrations criar banco a partir da model depois rodar python manage.py migrate
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    descricao = models.TextField()

    def __str__(self):#funcao parar retornar no painel administrador
        return self.nome  

    def teste():
        return 'Entrou'