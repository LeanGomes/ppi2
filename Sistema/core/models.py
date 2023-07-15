from django.db import models

# Create your models here.

#
# Criação da classe Registro da aplicação
class Registro(models.Model):
    codigo = models.CharField(primary_key=True,max_length=5)
    nome = models.CharField(max_length=50)
    horas= models.PositiveSmallIntegerField()


    def __str__(self):
        
        return (self.nome, self.horas)