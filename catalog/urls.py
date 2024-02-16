from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contact, catalog, product, cat_prod

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('product/<int:pk>', product, name='product'),
    path('<int:pk>/catalog/', cat_prod, name='cat_prod'),
    path('catalog/', catalog, name='catalog')
]
