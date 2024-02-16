from django.shortcuts import render

from catalog.models import Product, Category


# Create your views here.

def home(request):
    context = {
        'title': 'Домашняя',
        'cat_list': Category.objects.all()
    }
    return render(request, 'main/home.html', context)


def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{email} - {message}')
    context = {
        'title': 'Контакты',
        'cat_list': Category.objects.all()
    }
    return render(request, 'main/contact.html', context)


def catalog(request):
    context = {
        'object_list': Product.objects.all(),
        'cat_list': Category.objects.all(),
        'title': 'Каталог'
    }
    return render(request, 'main/catalog.html', context)


def cat_prod(request, pk):
    cat = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category=pk),
        'cat_list': Category.objects.all(),
        'title': f'{cat.name}'
    }
    return render(request, 'main/catalog.html', context)


def product(request, pk):
    prod = Product.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(pk=pk),
        'cat_list': Category.objects.all(),
        'title': f'{prod.name}'
    }
    return render(request, 'main/product.html', context)
