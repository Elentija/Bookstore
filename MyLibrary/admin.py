from django.contrib import admin

# Register your models here.
from MyLibrary.models import Client, Book, Author

admin.site.register(Client)
admin.site.register(Book)
admin.site.register(Author)