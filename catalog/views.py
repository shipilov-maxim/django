from django.shortcuts import render

from catalog.models import Product


# Create your views here.

def home(request):
    return render(request, 'main/home.html')


def contact(request):
    return render(request, 'main/contact.html')


def catalog(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list
    }
    return render(request, 'main/catalog.html', context)
