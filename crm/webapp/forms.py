from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . models import Record, Area

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput






#Login a user
        
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# - Create a record

class CreateRecordForm(forms.ModelForm):
    class Meta: 

        model = Record
        fields = ['first_name','last_name','email','phone', 'address', 'city', 'province', 'country']


# - Update a record

class UpdateRecordForm(forms.ModelForm):
    class Meta: 

        model = Record
        fields = ['first_name','last_name','email','phone', 'address', 'city', 'province', 'country']



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







