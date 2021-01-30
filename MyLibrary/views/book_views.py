from django.shortcuts import render, get_object_or_404, redirect
from MyLibrary.forms import BookForm
from MyLibrary.models import Book


def book_list(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'book/book_list.html', {'books': books})


def book_details(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book/book_details.html', {'book': book})


def book_new(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            book.save()
            return redirect('book_details.html', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'book/book_edit.html', {'form': form})