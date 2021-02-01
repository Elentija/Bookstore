from django.shortcuts import get_object_or_404, redirect, render
from MyLibrary.models import Book


def add_to_cart(request, pk):
    cart = request.session.get('cart')
    if not cart:
        cart = request.session['cart'] = list()

    book = get_object_or_404(Book, pk=pk)
    if book is not None:
        cart.append(book.pk)
        request.session['cart'] = cart
        book.quantity_in_watehause=-1

        books = list()
        cart_value = 0
        for x in cart:
            book = Book.objects.get(pk=x)
            books.append(book)
            cart_value += book.price
    return render(request, 'cart/cart.html', {'books': books, 'cart_value': cart_value})
    return redirect('book_list.html')


def cart_all(request):
    cart = request.session.get('cart')
    books = list()
    if not cart:
        cart = request.session['cart'] = list()
    cart_value = 0
    if len(cart) != 0:
        for x in cart:
            book = Book.objects.get(pk=x)
            books.append(book)
            cart_value += book.price
    return render(request, 'cart/cart.html', {'books': books, 'cart_value': cart_value})


def book_remove(request, pk):
    cart = request.session.get('cart')
    if pk in cart: cart.remove(pk)

    request.session['cart'] = cart
    books = list()
    cart_value = 0
    for x in cart:
        book = Book.objects.get(pk=x)
        books.append(book)
        cart_value += book.price
    return render(request, 'cart/cart.html', {'books': books, 'cart_value': cart_value})


