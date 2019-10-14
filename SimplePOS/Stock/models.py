from django.db import models
from datetime import datetime

# Create your models here.
class Categoria(models.Model):
    categoria = models.CharField(max_length=25, blank=False,null=True)

    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Categorias"
        verbose_name = "Categoria"

        def __str__(self):
            return self.categoria

class Marca(models.Model):
    marca = models.CharField(max_length=50,blank=False,null=True)
    def __str__(self):
        return self.marca

class Unmedida(models.Model):
    medida = models.CharField(max_length=30,blank=False,null=True)

    class Meta:
        ordering = ["medida"]
        verbose_name_plural = "Unidades de Medida"
        verbose_name = "Unidad de Medida"

        def __str__(self):
            return self.medida

class Formato(models.Model):
    formato = models.CharField(max_length=50,blank=False,null=True)
    cantidad = models.IntegerField(blank=False,null=True)
    medida = models.ForeignKey(Unmedida, on_delete=models.PROTECT)

class Proveedor(models.Model):
    rut = models.CharField(max_length=10,blank=False,null=True)
    nombre = models.CharField(max_length=100,blank=False,null=True)
    def __str__(self):
        return self.nombre

class Compra(models.Model):
    fecha = models.DateField(default=datetime.now,blank=True,null=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.id)

class Producto(models.Model):
    nombre = models.CharField(max_length=100,blank=False,null=True)
    barcode = models.CharField(max_length=20,blank=False,null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    formato = models.ForeignKey(Formato,on_delete=models.PROTECT)
    marca = models.ForeignKey(Marca,on_delete=models.PROTECT)
    def __str__(self):
        return self.nombre

class Detalle_compra(models.Model):
    compra = models.ForeignKey(Compra,null=True,on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,on_delete=models.PROTECT)
    cantidad = models.IntegerField(blank=False,null=True)

    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Detalle de Compras"
        verbose_name = "Detalle de Compra"

        def __str__(self):
            return self.compra


