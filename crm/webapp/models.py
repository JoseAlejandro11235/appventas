from django.db import models

class Record(models.Model):

    creation_date = models.DateTimeField(auto_now_add=True)

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    email = models.CharField(max_length=255)

    phone = models.CharField(max_length=20)

    address = models.CharField(max_length=300)

    city = models.CharField(max_length=255)

    province = models.CharField(max_length=200)

    country = models.CharField(max_length=125)

    def __str__(self):

        return self.first_name + "   " + self.last_name
    


class Area(models.Model):
 
    denominacion = models.CharField(max_length=100)

    def __str__(self):
        return self.denominacion


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    denominacion = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.denominacion 
    
    
class CategoriaPadre(models.Model):
    id_categoriahijo = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='categoria_padre_hijo', db_column='id_categoriahijo', to_field='id')
    id_categoriapadre = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='categoria_padre_padre', db_column='id_categoriapadre', to_field='id')


class Marca(models.Model):
    denominacion = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    def __str__(self):
        return self.denominacion
    

class UnidadMedida(models.Model):
    codigo_sunat = models.CharField(max_length=2)
    denominacion = models.CharField(max_length=100)

    def __str__(self):
         return self.denominacion
    

class Producto(models.Model):
    denominacion = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    id_unidad =  models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
    id_marca =  models.ForeignKey(Marca, on_delete=models.CASCADE)  

    def __str__(self):
        return self.denominacion


class ProductoCategoria(models.Model):
    id_producto =  models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_categoria =  models.ForeignKey(Categoria, on_delete=models.CASCADE)  


class ProductoPrecio(models.Model):
    precio = models.FloatField()
    fechavigencia = models.DateField()
    estado = models.BooleanField(default=False)
    id_producto =  models.ForeignKey(Producto, on_delete=models.CASCADE)



class TipoDocumento(models.Model):

    denominacion = models.CharField(max_length=100)
    codigo_sunat = models.CharField(max_length=2)

    def __str__(self):
         return self.denominacion
    


class Persona(models.Model):

    id_tipodocumento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)  
    documento = models.CharField(max_length=15)

    def str(self):
        return self.documento










