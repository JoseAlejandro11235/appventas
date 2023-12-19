from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . models import Record, Area, Categoria, CategoriaPadre, Marca, UnidadMedida, Producto, ProductoCategoria, ProductoPrecio, TipoDocumento, Persona

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


# - Update a Persona

class UpdatePersonaForm(forms.ModelForm):
    class Meta: 

        model = Persona
        fields = ['id_tipodocumento', 'documento']










