from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'main/home.html')


def contact(request):
    return render(request, 'main/contact.html')


def catalog(request):
    return render(request, 'main/catalog.html')
