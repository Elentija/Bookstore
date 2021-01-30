from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect

from MyLibrary.forms import ClientForm, ClientLoginForm
from MyLibrary.models import Client


def client_list(request):
    clients = Client.objects.all().order_by('last_name')
    return render(request, 'client/client_list.html', {'clients': clients})


def client_details(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'client/client_details.html', {'client': client})


def client_new(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save()
            form.save()
            return redirect('client_details.html', pk=client.pk)
    else:
        form = ClientForm()
    return render(request, 'client/client_edit.html', {'form': form})


def client_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('book_list')
        else:
            messages.info(request, 'Błędne dane! Spróbuj ponownie.')
            return redirect('client_login')
    else:
        form = ClientLoginForm()
        return render(request, 'client/client_login.html', {'form': form})


def client_register(request):
    if request.user.is_authenticated:
        messages.success(request, 'Już posiadasz konto')
        return redirect('client_register')
    else:
        if request.method == 'POST':
            form = ClientForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('book_list')
        else:
            form = ClientForm()
            return render(request, 'client/client_edit.html', {'form': form})


def client_logout(request):
    logout(request)
    messages.success(request, 'Zostałeś wylogowany!')
    return redirect('home')