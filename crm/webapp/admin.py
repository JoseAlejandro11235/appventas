from django.contrib import admin

# Register your models here.

from . models import Record, Area, Categoria, CategoriaPadre, Marca, UnidadMedida, Producto, ProductoCategoria, ProductoPrecio,TipoDocumento, Persona, Operador


admin.site.register(Record)
admin.site.register(Area)
admin.site.register(Categoria)
admin.site.register(CategoriaPadre)
admin.site.register(Marca)
admin.site.register(UnidadMedida)
admin.site.register(Producto)
admin.site.register(ProductoCategoria)
admin.site.register(ProductoPrecio)
admin.site.register(TipoDocumento)
admin.site.register(Persona)
admin.site.register(Operador)



