from django.shortcuts import render

from catalog.models import Product


# Create your views here.

def home(request):
    context = {
        'title': 'Домашняя'
    }
    return render(request, 'main/home.html', context)


def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{email} - {message}')
    context = {
        'title': 'Контакты'
    }
    return render(request, 'main/contact.html', context)


def catalog(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Каталог'
    }
    return render(request, 'main/catalog.html', context)


def product(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Продукт'
    }
    return render(request, 'main/product.html', context)
