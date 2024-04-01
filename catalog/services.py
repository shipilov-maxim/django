from django.core.cache import cache
from catalog.models import Category, Product
from config.settings import CACHE_ENABLED


def cache_category():
    if not CACHE_ENABLED:
        return Category.objects.all()
    key = "categories_list"
    categories = cache.get(key)
    if categories is None:
        categories = Category.objects.all()
        cache.set(key, categories)
    return categories


def cache_product_staff():
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "products_list_staff"
    products = cache.get(key)
    if products is None:
        products = Product.objects.all()
        cache.set(key, products)
    return products


def cache_product():
    if not CACHE_ENABLED:
        return Product.objects.all().filter(is_published=True)
    key = "products_list"
    products = cache.get(key)
    if products is None:
        products = Product.objects.all().filter(is_published=True)
        cache.set(key, products)
    return products
