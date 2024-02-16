from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contact, catalog, product

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('product/', product, name='product'),
    path('catalog/', catalog, name='catalog')
]
