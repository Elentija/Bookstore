from django.contrib import admin

# Register your models here.
from MyLibrary.models import Client, Book, Author, Order

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Order)