from django.db import models

# Create your models here.
class Sala(models.Model):
        nome = models.CharField(max_length=100)
        numsala = models.IntegerField()
        andar = models.IntegerField()
        recursos = models.CharField(max_length=100)
        capacidade = models.IntegerField()
        def __str__(self):
            return f"{self.nome, self.recursos}"
class Usuario(models.Model):
      nome = models.CharField(max_length=100)
      cpf = models.CharField(max_length=100)
      email = models.CharField(max_length=100)
      ativo = models.BooleanField()
      nivel = models.CharField(max_length=100)
      def __str__(self):
            return f"{self.nome, self.nivel}"
      
class Reserva(models.Model):
      sala = models.IntegerField()
      usuario = models.CharField(max_length=100)
      data = models.DateTimeField()
      status = models.CharField(max_length=100)