from datetime import datetime

from django.db import models

# Create your models here.

class Sucursal(models.Model):
    name = models.CharField(max_length=50)
    ipaddress = models.CharField(max_length=15)
    port = models.PositiveIntegerField()
    operators = models.CharField(max_length=200, default='isranyag')        #Se ingresa los usuarios permitidos separados por coma, sin espacio

    def __str__(self):
        return self.name


class Logg(models.Model):
    id  = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(default=datetime.now())
    operador = models.CharField(max_length=100)
    accion = models.CharField(max_length=250)
    sucursal = models.CharField(max_length=50)

    def __str__(self):
        log = str(self.sucursal) + ' - ' + str(self.accion) + ' ' + str(self.fecha) + ' por ' + str(self.operador)
        return log