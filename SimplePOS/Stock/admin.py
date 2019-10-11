from django.contrib import admin
from Stock.models import Categoria,Marca,Unmedida,Formato,Producto,Proveedor,Compra,Detalle_compra 


# Register your models here.
admin.site.register(Categoria),
admin.site.register(Marca),
admin.site.register(Unmedida),
admin.site.register(Formato),
admin.site.register(Producto),
admin.site.register(Proveedor),
admin.site.register(Compra),
admin.site.register(Detalle_compra),

