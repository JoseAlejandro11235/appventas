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
        return str(self.pk)

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
    def __str__(self):
        return str(self.pk)


class ProductoPrecio(models.Model):
    precio = models.FloatField()
    fechavigencia = models.DateField()
    estado = models.BooleanField(default=False)
    id_producto =  models.ForeignKey(Producto, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.precio)




class TipoDocumento(models.Model):

    denominacion = models.CharField(max_length=100)
    codigo_sunat = models.CharField(max_length=2)

    def __str__(self):
         return self.denominacion
    


class Persona(models.Model):
    id_tipodocumento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)  
    documento = models.CharField(max_length=15)

    def __str__(self):
        return self.documento
    
class Operador(models.Model):
    denominacion=models.CharField(max_length=100)
    def __str__(self):
        return self.denominacion






class TipoTelefono(models.Model):
    denominacion=models.CharField(max_length=100)
    def __str__(self):
        return self.denominacion

class Telefono(models.Model):
    numero = models.CharField(max_length=100)
    id_operador = models.ForeignKey(Operador, on_delete=models.CASCADE)  
    id_tipotelefono = models.ForeignKey(TipoTelefono, on_delete=models.CASCADE)  
    def __str__(self):
        return self.numero

class PersonaTelefono(models.Model):
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE)  
    id_telefono = models.ForeignKey(Telefono, on_delete=models.CASCADE)  
    def __str__(self):
        return str(self.pk)


class Ubigeo(models.Model):
    ubigeo =  models.CharField(max_length=6, primary_key=True)
    departamento = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    distrito = models.CharField(max_length=100)
    def __str__(self):
        return self.ubigeo

class TipoVia(models.Model):
    codigo_sunat = models.CharField(max_length=2)
    denominacion = models.CharField(max_length=100)
    def __str__(self):
        return self.denominacion

class TipoZona(models.Model):
    codigo_sunat = models.CharField(max_length=2)
    denominacion = models.CharField(max_length=100)
    def __str__(self):
        return self.denominacion

class Direccion(models.Model):
    id_tipozona = models.ForeignKey(TipoZona, on_delete=models.CASCADE)  
    id_tipovia = models.ForeignKey(TipoVia, on_delete=models.CASCADE)  
    id_ubigeo = models.ForeignKey(Ubigeo, on_delete=models.CASCADE)  
    nombre_zona = models.CharField(max_length=100)
    nombre_via = models.CharField(max_length=100)
    manzana = models.CharField(max_length=2)
    lote = models.CharField(max_length=2)
    numero = models.CharField(max_length=6)
    def __str__(self):
        return self.nombre_zona + ' ' + self.nombre_via + ' ' +'manzana' + ' '+self.manzana +  'lote' + ' ' + self.lote + 'numero' + self.numero

class TipoDireccion(models.Model):
    denominacion = models.CharField(max_length=100)
    def __str__(self):
        return self.denominacion

class PersonaDireccion(models.Model):
    id_direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE) 
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE) 
    id_tipodireccion = models.ForeignKey(TipoDireccion, on_delete=models.CASCADE) 
    def __str__(self):
        return str(self.pk)




class PersonaJuridica(models.Model):
    id_persona =  models.ForeignKey(Persona, on_delete=models.CASCADE, primary_key=True)
    razon_social = models.CharField(max_length=100)
    nombre_comercial = models.CharField(max_length=100)
    sitio_web = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre_comercial

class Sexo(models.Model):
    codigo_sunat = models.CharField(max_length=2)
    denominacion = models.CharField(max_length=100)
    def __str__(self):
        return self.denominacion

class Nacionalidad(models.Model):
    codigo_sunat = models.CharField(max_length=2)
    denominacion = models.CharField(max_length=100)
    def __str__(self):
        return self.denominacion


class PersonaNatural(models.Model):
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE, primary_key=True)
    nombres = models.CharField(max_length=100)
    apaterno = models.CharField(max_length=100)
    amaterno = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    id_sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE) 
    id_nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombres


class Sucursal(models.Model):
    id_direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE) 
    descripcion = models.CharField(max_length=100)
    def __str__(self):
        return self.descripcion

class Cargo(models.Model):
    denominacion = models.CharField(max_length=100)
    id_area = models.ForeignKey(Area, on_delete=models.CASCADE) 
    def __str__(self):
        return self.denominacion

class Rol(models.Model):
    denominacion = models.CharField(max_length=100)
    def __str__(self):
        return self.denominacion


class Empleado(models.Model):
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE) 
    id_cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE) 
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE) 
    id_sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE) 
    def __str__(self):
        return str(self.id_persona)


class TipoCliente(models.Model):
    denominacion = models.CharField(max_length=100)
    def __str__(self):
        return self.denominacion



class Cliente(models.Model):
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE, primary_key=True)
    id_tipocliente = models.ForeignKey(TipoCliente, on_delete=models.CASCADE) 
    def __str__(self):
        return str(self.id_persona)

class Proveedor(models.Model):
    id_persona = models.ForeignKey(Persona, on_delete = models.CASCADE)
    def __str__(self):
        return str(self.id_persona)

class Venta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    subtotal = models.FloatField()
    igv = models.FloatField()
    total = models.FloatField()
    id_vendedor = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='vendedor_ventas')
    id_cajero = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='cajero_ventas')
    id_cliente =  models.ForeignKey(Cliente, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.pk)

class DetalleVenta(models.Model):
    id_venta = models.ForeignKey(Venta, on_delete = models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete = models.CASCADE)
    id_productoprecio = models.ForeignKey(ProductoPrecio,  on_delete = models.CASCADE)
    subtotal = models.FloatField()
    def __str__(self):
        return str(self.pk)

class TipoComprobante(models.Model):
    codigo_sunat = models.CharField(max_length=2)
    denominacion = models.CharField(max_length=100)
    def __str__(self):
        return self.denominacion

class SucursalSerie(models.Model):
    serie = models.CharField(max_length=12, primary_key=True)
    id_sucursal = models.ForeignKey(Sucursal, on_delete = models.CASCADE)
    id_tipocomprobante = models.ForeignKey(TipoComprobante,  on_delete = models.CASCADE)
    def __str__(self):
        return str(self.pk) 

class ComprobanteVenta(models.Model):
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    serie =models.ForeignKey(SucursalSerie, on_delete=models.CASCADE)
    correlativo = models.CharField(max_length=100)
    def __str__(self):
        return str(self.pk)

class Compra(models.Model):
    serie = models.CharField(max_length=12)
    correlativo = models.CharField(max_length=12)
    fecha = models.DateTimeField(auto_now_add=True)
    subtotal = models.FloatField()
    igv = models.FloatField()
    total = models.FloatField()
    id_tipocomprobante = models.ForeignKey(TipoComprobante, on_delete=models.CASCADE)
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.pk)     

class DetalleCompra(models.Model):
    id_compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.FloatField()
    precio_unitario = models.FloatField()
    subtotal = models.FloatField()
    def __str__(self):
        return str(self.pk)



class Oficio(models.Model):
    codigo_sunat = models.CharField(max_length=2)
    denominacion = models.CharField(max_length=100)
    def __str__(self):
        return self.denominacion

class PersonaOficio(models.Model):
    id_oficio = models.ForeignKey(Oficio, on_delete=models.CASCADE)
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.pk)

    