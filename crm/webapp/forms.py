from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . models import Record, Area, Categoria, CategoriaPadre, Marca, UnidadMedida, Producto, ProductoCategoria, ProductoPrecio, TipoDocumento, Persona, Operador, TipoTelefono, Telefono, PersonaTelefono, Ubigeo, TipoVia, TipoZona, Direccion, TipoDireccion, PersonaDireccion, PersonaJuridica, Sexo, Nacionalidad, PersonaNatural, Sucursal, Cargo, Rol, Empleado, TipoCliente, Cliente, Proveedor, Venta, DetalleVenta, TipoComprobante, SucursalSerie, ComprobanteVenta, Compra, DetalleCompra, Oficio, PersonaOficio

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput






#Login a user
        
class LoginForm(AuthenticationForm):

    username = forms.CharField(label='Usuario', widget=TextInput())
    password = forms.CharField(label='Contraseña', widget=PasswordInput())


# - Create a record

class CreateRecordForm(forms.ModelForm):
    class Meta: 

        model = Record
        fields = ['first_name','last_name','email','phone', 'address', 'city', 'province', 'country']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo Electrónico',
            'phone': 'Teléfono',
            'address': 'Dirección',
            'city': 'Ciudad',
            'province': 'Provincia',
            'country': 'País',
        }


# - Update a record

class UpdateRecordForm(forms.ModelForm):
    class Meta: 

        model = Record
        fields = ['first_name','last_name','email','phone', 'address', 'city', 'province', 'country']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo Electrónico',
            'phone': 'Teléfono',
            'address': 'Dirección',
            'city': 'Ciudad',
            'province': 'Provincia',
            'country': 'País',
        }



# - Create an area

class CreateAreaForm(forms.ModelForm):
    class Meta:

        model = Area
        fields = ['denominacion']


# - Update an area

class UpdateAreaForm(forms.ModelForm):
    class Meta: 

        model = Area
        fields = ['denominacion']


# - Create a categoria

class CreateCategoriaForm(forms.ModelForm):
    class Meta:

        model = Categoria
        fields = ['denominacion', 'descripcion']


# - Update a categoria

class UpdateCategoriaForm(forms.ModelForm):
    class Meta: 

        model = Categoria
        fields = ['denominacion', 'descripcion']




# - Create a categoria padre

class CreateCategoriaPadreForm(forms.ModelForm):
    class Meta:

        model = CategoriaPadre
        fields = ['id_categoriahijo', 'id_categoriapadre']


# - Update a categoria padre

class UpdateCategoriaPadreForm(forms.ModelForm):
    class Meta: 

        model = CategoriaPadre
        fields = ['id_categoriahijo', 'id_categoriapadre']



# - Create a marca

class CreateMarcaForm(forms.ModelForm):
    class Meta:

        model = Marca
        fields = ['denominacion', 'descripcion']


# - Update a marca

class UpdateMarcaForm(forms.ModelForm):
    class Meta: 

        model = Marca
        fields = ['denominacion', 'descripcion']


# - Create a marca

class CreateUnidadMedidaForm(forms.ModelForm):
    class Meta:

        model = UnidadMedida
        fields = ['codigo_sunat', 'denominacion']


# - Update a marca

class UpdateUnidadMedidaForm(forms.ModelForm):
    class Meta: 

        model = UnidadMedida
        fields = ['codigo_sunat', 'denominacion']


# - Create a Producto

class CreateProductoForm(forms.ModelForm):
    class Meta:

        model = Producto
        fields = ['denominacion', 'descripcion', 'id_unidad', 'id_marca']



# - Update a marca

class UpdateProductoForm(forms.ModelForm):
    class Meta: 

        model = Producto
        fields = ['denominacion', 'descripcion', 'id_unidad', 'id_marca']


# - Create a Producto Categoria

class CreateProductoCategoriaForm(forms.ModelForm):
    class Meta:

        model = ProductoCategoria
        fields = ['id_producto', 'id_categoria']



# - Update a Producto Categoria

class UpdateProductoCategoriaForm(forms.ModelForm):
    class Meta: 

        model = ProductoCategoria
        fields = ['id_producto', 'id_categoria']


# - Create a Producto Precio

class CreateProductoPrecioForm(forms.ModelForm):
    class Meta:

        model = ProductoPrecio
        fields = ['precio', 'fechavigencia','estado','id_producto']



# - Update a Producto Precio

class UpdateProductoPrecioForm(forms.ModelForm):
    class Meta: 

        model = ProductoPrecio
        fields = ['precio', 'fechavigencia','estado','id_producto']


# - Create a Tipo Documento

class CreateTipoDocumentoForm(forms.ModelForm):
    class Meta:

        model = TipoDocumento
        fields = ['denominacion', 'codigo_sunat']


# - Update a Tipo Documento

class UpdateTipoDocumentoForm(forms.ModelForm):
    class Meta: 

        model = TipoDocumento
        fields = ['denominacion', 'codigo_sunat']


# - Create a Persona

class CreatePersonaForm(forms.ModelForm):
    class Meta:

        model = Persona
        fields = ['id_tipodocumento', 'documento']


# - Update an Persona

class UpdatePersonaForm(forms.ModelForm):
    class Meta: 

        model = Persona
        fields = ['id_tipodocumento', 'documento']


# - Create a Operador

class CreateOperadorForm(forms.ModelForm):
    class Meta:

        model = Operador
        fields = ['denominacion']


# - Update an Operador

class UpdateOperadorForm(forms.ModelForm):
    class Meta: 

        model = Operador
        fields = ['denominacion']


# - Create a Tipo Teléfono

class CreateTipoTelefonoForm(forms.ModelForm):
    class Meta:

        model = TipoTelefono
        fields = ['denominacion']


# - Update a Tipo Teléfono

class UpdateTipoTelefonoForm(forms.ModelForm):
    class Meta: 

        model = TipoTelefono
        fields = ['denominacion']






# - Create a categoria padre

class CreateCategoriaPadreForm(forms.ModelForm):
    class Meta:

        model = CategoriaPadre
        fields = ['id_categoriahijo', 'id_categoriapadre']


# - Update a categoria padre

class UpdateCategoriaPadreForm(forms.ModelForm):
    class Meta: 

        model = CategoriaPadre
        fields = ['id_categoriahijo', 'id_categoriapadre']



# - Create a marca

class CreateMarcaForm(forms.ModelForm):
    class Meta:

        model = Marca
        fields = ['denominacion', 'descripcion']


# - Update a marca

class UpdateMarcaForm(forms.ModelForm):
    class Meta: 

        model = Marca
        fields = ['denominacion', 'descripcion']



#************************************ From here begins the work

#************************************

#************************************

#************************************

#************************************
        
# - Create a Teléfono

class CreateTelefonoForm(forms.ModelForm):
    class Meta:

        model = Telefono
        fields = ['numero', 'id_operador', 'id_tipotelefono']


# - Update a Teléfono

class UpdateTelefonoForm(forms.ModelForm):
    class Meta: 

        model = Telefono
        fields = ['numero', 'id_operador', 'id_tipotelefono']


# - Create a Persona Teléfono

class CreatePersonaTelefonoForm(forms.ModelForm):
    class Meta:

        model = PersonaTelefono
        fields = ['id_persona', 'id_telefono']


# - Update a Persona Teléfono

class UpdatePersonaTelefonoForm(forms.ModelForm):
    class Meta: 

        model = PersonaTelefono
        fields = ['id_persona', 'id_telefono']


# - Create a Ubigeo

class CreateUbigeoForm(forms.ModelForm):
    class Meta:

        model = Ubigeo
        fields = ['ubigeo', 'departamento','provincia', 'distrito']


# - Update a Ubigeo

class UpdateUbigeoForm(forms.ModelForm):
    class Meta: 

        model = Ubigeo
        fields = ['ubigeo', 'departamento','provincia', 'distrito']


# - Create a Tipo Via

class CreateTipoViaForm(forms.ModelForm):
    class Meta:

        model = TipoVia
        fields = ['codigo_sunat', 'denominacion']


# - Update a Tipo Via

class UpdateTipoViaForm(forms.ModelForm):
    class Meta: 

        model = TipoVia
        fields = ['codigo_sunat', 'denominacion']


# - Create a Tipo Zona

class CreateTipoZonaForm(forms.ModelForm):
    class Meta:

        model = TipoZona
        fields = ['codigo_sunat', 'denominacion']


# - Update a Tipo Zona

class UpdateTipoZonaForm(forms.ModelForm):
    class Meta: 

        model = TipoZona
        fields = ['codigo_sunat', 'denominacion']


# - Create a Direccion

class CreateDireccionForm(forms.ModelForm):
    class Meta:

        model = Direccion
        fields = ['id_tipozona', 'id_tipovia','id_ubigeo','nombre_zona','nombre_via', 'manzana', 'lote', 'numero']


# - Update a Direccion

class UpdateDireccionForm(forms.ModelForm):
    class Meta: 

        model = Direccion
        fields = ['id_tipozona', 'id_tipovia','id_ubigeo','nombre_zona','nombre_via', 'manzana', 'lote', 'numero']


# - Create a Tipo Direccion

class CreateTipoDireccionForm(forms.ModelForm):
    class Meta:

        model = TipoDireccion
        fields = ['denominacion']


# - Update a Tipo Direccion

class UpdateTipoDireccionForm(forms.ModelForm):
    class Meta: 

        model = TipoDireccion
        fields = ['denominacion']


# - Create a Persona Direccion

class CreatePersonaDireccionForm(forms.ModelForm):
    class Meta:

        model = PersonaDireccion
        fields = ['id_direccion','id_persona','id_tipodireccion']


# - Update a Persona Direccion

class UpdatePersonaDireccionForm(forms.ModelForm):
    class Meta: 

        model = PersonaDireccion
        fields = ['id_direccion','id_persona','id_tipodireccion']


# - Create a Persona Juridica

class CreatePersonaJuridicaForm(forms.ModelForm):
    class Meta:

        model = PersonaJuridica
        fields = ['id_persona','razon_social','nombre_comercial','sitio_web']


# - Update a Persona Juridica

class UpdatePersonaJuridicaForm(forms.ModelForm):
    class Meta: 

        model = PersonaJuridica
        fields = ['id_persona','razon_social','nombre_comercial','sitio_web']



# - Create a Sexo
        
class CreateSexoForm(forms.ModelForm):
    class Meta:

        model = Sexo
        fields = ['codigo_sunat','denominacion']


# - Update a Sexo

class UpdateSexoForm(forms.ModelForm):
    class Meta: 

        model = Sexo
        fields = ['codigo_sunat','denominacion']



# - Create a Nacionalidad
        
class CreateNacionalidadForm(forms.ModelForm):
    class Meta:

        model = Nacionalidad
        fields = ['codigo_sunat','denominacion']


# - Update a Nacionalidad

class UpdateNacionalidadForm(forms.ModelForm):
    class Meta: 

        model = Nacionalidad
        fields = ['codigo_sunat','denominacion']



# - Create a Persona Natural
        
class CreatePersonaNaturalForm(forms.ModelForm):
    class Meta:

        model = PersonaNatural
        fields = ['id_persona','nombres','apaterno','amaterno','fecha_nacimiento','id_sexo','id_nacionalidad']


# - Update a Persona Natural

class UpdatePersonaNaturalForm(forms.ModelForm):
    class Meta: 

        model = PersonaNatural
        fields = ['id_persona','nombres','apaterno','amaterno','fecha_nacimiento','id_sexo','id_nacionalidad']



# - Create a Sucursal
        
class CreateSucursalForm(forms.ModelForm):
    class Meta:

        model = Sucursal
        fields = ['id_direccion','descripcion']


# - Update a Sucursal

class UpdateSucursalForm(forms.ModelForm):
    class Meta: 

        model = Sucursal
        fields = ['id_direccion','descripcion']



# - Create a Cargo
        
class CreateCargoForm(forms.ModelForm):
    class Meta:

        model = Cargo
        fields = ['denominacion','id_area']


# - Update a Cargo

class UpdateCargoForm(forms.ModelForm):
    class Meta: 

        model = Cargo
        fields = ['denominacion','id_area']



# - Create a Rol
        
class CreateRolForm(forms.ModelForm):
    class Meta:

        model = Rol
        fields = ['denominacion']


# - Update a Rol

class UpdateRolForm(forms.ModelForm):
    class Meta: 

        model = Rol
        fields = ['denominacion']



# - Create a Empleado
        
class CreateEmpleadoForm(forms.ModelForm):
    class Meta:

        model = Empleado
        fields = ['id_persona','id_cargo','id_rol','id_sucursal']


# - Update a Empleado

class UpdateEmpleadoForm(forms.ModelForm):
    class Meta: 

        model = Empleado
        fields = ['id_persona','id_cargo','id_rol','id_sucursal']



# - Create a TipoCliente
        
class CreateTipoClienteForm(forms.ModelForm):
    class Meta:

        model = TipoCliente
        fields = ['denominacion']


# - Update a TipoCliente

class UpdateTipoClienteForm(forms.ModelForm):
    class Meta: 

        model = TipoCliente
        fields = ['denominacion']



# - Create a Cliente
        
class CreateClienteForm(forms.ModelForm):
    class Meta:

        model = Cliente
        fields = ['id_persona', 'id_tipocliente']


# - Update a Cliente

class UpdateClienteForm(forms.ModelForm):
    class Meta: 

        model = Cliente
        fields = ['id_persona', 'id_tipocliente']



# - Create a Proveedor
        
class CreateProveedorForm(forms.ModelForm):
    class Meta:

        model = Proveedor
        fields = ['id_persona']


# - Update a Proveedor

class UpdateProveedorForm(forms.ModelForm):
    class Meta: 

        model = Proveedor
        fields = ['id_persona']



# - Create a Venta
        
class CreateVentaForm(forms.ModelForm):
    class Meta:

        model = Venta
        fields = ['subtotal','igv','total','id_vendedor','id_cajero','id_cliente']


# - Update a Venta

class UpdateVentaForm(forms.ModelForm):
    class Meta: 

        model = Venta
        fields = ['subtotal','igv','total','id_vendedor','id_cajero','id_cliente']


# - Create a Detalle Venta
        
class CreateDetalleVentaForm(forms.ModelForm):
    class Meta:

        model = DetalleVenta
        fields = ['id_venta','id_producto','id_productoprecio','cantidad','subtotal']


# - Update a Detalle Venta

class UpdateDetalleVentaForm(forms.ModelForm):
    class Meta: 

        model = DetalleVenta
        fields = ['id_venta','id_producto','id_productoprecio','cantidad','subtotal']



# - Create a Tipo Comprobante
        
class CreateTipoComprobanteForm(forms.ModelForm):
    class Meta:

        model = TipoComprobante
        fields = ['codigo_sunat','denominacion']


# - Update a Tipo Comprobante

class UpdateTipoComprobanteForm(forms.ModelForm):
    class Meta: 

        model = TipoComprobante
        fields = ['codigo_sunat','denominacion']



# - Create a Sucursal Serie
        
class CreateSucursalSerieForm(forms.ModelForm):
    class Meta:

        model = SucursalSerie
        fields = ['serie','id_sucursal','id_tipocomprobante']


# - Update a Sucursal Serie

class UpdateSucursalSerieForm(forms.ModelForm):
    class Meta: 

        model = SucursalSerie
        fields = ['serie','id_sucursal','id_tipocomprobante']




# - Create a ComprobanteVenta
        
class CreateComprobanteVentaForm(forms.ModelForm):
    class Meta:

        model = ComprobanteVenta
        fields = ['id_venta','serie','correlativo']


# - Update a Comprobante Venta

class UpdateComprobanteVentaForm(forms.ModelForm):
    class Meta: 

        model = ComprobanteVenta
        fields = ['id_venta','serie','correlativo']


# - Create a Compra
        
class CreateCompraForm(forms.ModelForm):
    class Meta:

        model = Compra
        fields = ['serie','correlativo','subtotal','igv','total','id_tipocomprobante','id_proveedor']


# - Update a Compra

class UpdateCompraForm(forms.ModelForm):
    class Meta: 

        model = Compra
        fields = ['serie','correlativo','subtotal','igv','total','id_tipocomprobante','id_proveedor']



# - Create a DetalleCompra
        
class CreateDetalleCompraForm(forms.ModelForm):
    class Meta:

        model = DetalleCompra
        fields = ['id_compra','id_producto','cantidad','precio_unitario','subtotal']


# - Update a DetalleCompra

class UpdateDetalleCompraForm(forms.ModelForm):
    class Meta: 

        model = DetalleCompra
        fields = ['id_compra','id_producto','cantidad','precio_unitario','subtotal']



# - Create a Oficio
        
class CreateOficioForm(forms.ModelForm):
    class Meta:

        model = Oficio
        fields = ['codigo_sunat','denominacion']


# - Update a Oficio

class UpdateOficioForm(forms.ModelForm):
    class Meta: 

        model = Oficio
        fields = ['codigo_sunat','denominacion']




# - Create a Persona Oficio Oficio
        
class CreatePersonaOficioForm(forms.ModelForm):
    class Meta:

        model = PersonaOficio
        fields = ['id_oficio','id_persona']


# - Update a PersonaOficio

class UpdatePersonaOficioForm(forms.ModelForm):
    class Meta: 

        model = PersonaOficio
        fields = ['id_oficio','id_persona']

