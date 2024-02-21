from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Product, Category


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
        'title': 'Контакты',
        'cat_list': Category.objects.all()
    }
    return render(request, 'main/contact.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'main/catalog.html'


class CategoryListView(ListView):
    model = Category
    template_name = 'main/categories.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product.html'


def cat_prod(request, pk):
    category = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category=pk),
        'title': f'{category.name}'
    }
    return render(request, 'main/catalog.html', context)

# class CategoryDetailView(DetailView):
#     model = Category
#     template_name = 'main/catalog.html'
