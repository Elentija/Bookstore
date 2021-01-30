from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Client, Book, Address, Delivery


class ClientForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')

    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'login', 'password', 'password2')


class ClientLoginForm(forms.Form):
    login = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'rate', 'price', 'release_date', 'quantity_in_watehause', 'category')


class NewAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['city', 'street', 'number', 'zip_code']


class NewDeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['price', 'address', 'order', 'delivery_method']