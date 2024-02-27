from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, CategoryListView, HomePageView, ContactView, \
    CategoryDetailView, BlogDetailView, BlogListView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('catalog/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('catalog/', ProductListView.as_view(), name='catalog'),
    path('categories/<int:pk>', CategoryDetailView.as_view(), name='cat_prod'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('blog/<slug>', BlogDetailView.as_view(), name='blog'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('update/<slug>', BlogUpdateView.as_view(), name='blog_update'),
    path('delete/<slug>', BlogDeleteView.as_view(), name='blog_delete'),
]
