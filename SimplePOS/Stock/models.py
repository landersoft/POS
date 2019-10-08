from django.db import models

# Create your models here.
class Categoria(models.Model):
    categoria = models.CharField(max_length=25)
    def __str__(self):
        return self.categoria

class Marca(models.Model):
    marca = models.CharField(max_length=50)
    def __str__(self):
        return self.marca

class Unmedida(models.Model):
    medida = models.CharField(max_length=30)
    def __str__(self):
        return self.medida

class Formato(models.Model):
    formato = models.CharField(max_length=50),
    cantidad = models.IntegerField(),
    medida = models.ForeignKey(Unmedida)

class Proveedor(models.Model):
    rut = models.CharField(max_length=10),
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Compra(models.Model):
    fecha = models.DateField(),
    proveedor = models.ForeignKey(Proveedor)
    def __str__(self):
        return str(self.id)

class Producto(models.Model):
    nombre = models.CharField(max_length=100),
    barcode = models.CharField(max_length=20),
    categoria = models.ForeignKey(Categoria),
    formato = models.ForeignKey(Formato),
    marca = models.ForeignKey(Marca)
    def __str__(self):
        return self.nombre

class Detalle_compra(models.Model):
    compra = models.ForeignKey(Compra),
    producto = models.ForeignKey(Producto),
    cantidad = models.IntegerField()
    def __str__(self):
        return self.compra


