from django.db import models

# Create your models here.
class Bebida(models.Model):
    nombre=models.CharField(max_length=30)
    sabor=models.CharField(max_length=30)
    marca=models.CharField(max_length=30)
    calorias = models.IntegerField()
    fecha_creado = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre}-{self.marca}-{self.fecha_creado}"