from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . models import Record

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





