from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contact, ProductListView, ProductDetailView, CategoryListView, cat_prod

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('catalog/<int:pk>', cat_prod, name='cat_prod'),
    path('catalog/', ProductListView.as_view(), name='catalog'),
    path('categories/', CategoryListView.as_view(), name='categories')
]
