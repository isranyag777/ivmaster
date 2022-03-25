from django.db import models

# Create your models here.

class Usuario(models.Model):
    username = models.CharField(primary_key=True, max_length=7)
    password = models.CharField(max_length=14)
    maxconn = models.IntegerField(default=1)
    bouquet = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Sucursal(models.Model):
    name = models.CharField(max_length=50)
    ipaddress = models.CharField(max_length=15)
    port = models.PositiveIntegerField()
    operators = models.CharField(max_length=200, default='isranyag')        #Se ingresa los usuarios permitidos separados por coma, sin espacio

    def __str__(self):
        return self.name