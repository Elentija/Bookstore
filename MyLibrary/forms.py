from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Client, Book, Address, Delivery, BookRating


class ClientForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


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


class RatingForm(forms.ModelForm):
    class Meta:
        model = BookRating
        fields = ('book', 'client', 'rate')

