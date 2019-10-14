from django.db import models
from Stock.models import Producto
from datetime import datetime   
# Create your models here.

class Venta(models.Model):
    fecha = models.DateTimeField(default=datetime.now())
    def __str__(self):
        return str(self.id)

class DetalleVenta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    venta = models.ForeignKey(Venta, on_delete=models.PROTECT)
    cantidad = models.IntegerField(blank=False, null=True)
    def __str__(self):
        return self.venta


