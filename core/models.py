from django.db import models

# Create your models here.

class Recurso(models.Model):
        nome = models.CharField(max_length=100)
       
        def __str__(self):
            return f"{self.nome}"
class Sala(models.Model):
        numsala = models.IntegerField()
        
        capacidade = models.IntegerField()
        recursos = models.ManyToManyField(Recurso, blank=True)
        disponivel = models.BooleanField(default=True)
        dia_nao_disponivel = models.DateField(blank=True, null=True)
        preco = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

        def __str__(self):
            return f"{self.numsala}"
class Usuario(models.Model):
      nome = models.CharField(max_length=100)
      cpf = models.CharField(max_length=100)
      email = models.CharField(max_length=100)
      ativo = models.BooleanField(default=True)
      nivel = models.CharField(max_length=100, default="1")
      foto_perfil = models.URLField(blank=True, null=True)
      def __str__(self):
            return f"{self.nome, self.nivel}"
      
class Reserva(models.Model):
      usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
      sala = models.ForeignKey(Sala, on_delete=models.PROTECT)
      data_reserva = models.DateField(default=None)
      hora_inicio = models.TimeField(default=None)
      hora_fim = models.TimeField(default=None)
      multa = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
      preco_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
      def __str__(self):
            return f"{self.usuario.nome} reservou a sala {self.sala.numsala} no dia {self.data_reserva} das {self.hora_inicio} às {self.hora_fim}"