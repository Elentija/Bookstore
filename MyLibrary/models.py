from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=60)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=60)
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)
    rate = models.DecimalField(max_digits=2, decimal_places=1)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    release_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    quantity_in_watehause = models.IntegerField()

    BookCategory = (
        ('Fantazy', 'FANTAZY'),
        ('Obyczajowe', 'OBYCZJOWE'),
        ('Historyczne', 'HISTORYCZNE')
    )
    category = models.CharField(max_length=30, choices=BookCategory)

    def __str__(self):
        return f"{self.title}"

    def serialize(self):
        return self.__dict__


class Order(models.Model):
    order_value = models.DecimalField(max_digits=7, decimal_places=2)
    date_of_submission = models.DateTimeField(auto_now=False, auto_now_add=False)
    client = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.pk}: Wartość: {self.order_value}"


class ProductsInBasket(models.Model):
    product = models.ForeignKey(Book, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product}"

    def serialize(self):
        return self.__dict__


class Payment(models.Model):
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)

    PaymentMethod = (
        ("Blik", "BLIK"),
        ("Przelew", "PRZELEW"),
        ("Gotówka", "GOTÓWKA")
    )
    payment_method = models.CharField(max_length=30, choices=PaymentMethod)

    def __str__(self):
        return f"{self.payment_method}"


class Address(models.Model):
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    number = models.IntegerField()
    zip_code = models.CharField("zip code", max_length=5, default="43701")

    def __str__(self):
        return f"{self.zip_code} {self.city}"


class Delivery(models.Model):
    price = models.DecimalField(max_digits=5, decimal_places=2)
    address = models.ForeignKey(Address, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    DeliveryMethod = (
        ("Kurier", "KURIER"),
        ("Paczkomat", "PACZKOMAT"),
        ("Poczta", "POCZTA")
    )
    delivery_method = models.CharField(max_length=30, choices=DeliveryMethod)

    def __str__(self):
        return f"{self.delivery_method}"


class BookRating(models.Model):
    book = models.ForeignKey(Book, null=True, on_delete=models.SET_NULL)
    client = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    rate = models.IntegerField()
