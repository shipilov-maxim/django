from django.urls import path
from django.views.decorators.cache import cache_page
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, CategoryListView, HomePageView, ContactView, \
    CategoryDetailView, BlogDetailView, BlogListView, BlogCreateView, BlogUpdateView, BlogDeleteView, \
    toggle_published, ProductCreateView, ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('catalog/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('create_product/', ProductCreateView.as_view(), name='product_create'),
    path('update_product/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('catalog/', ProductListView.as_view(), name='catalog'),
    path('categories/<int:pk>', CategoryDetailView.as_view(), name='cat_prod'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('blog/<slug>', BlogDetailView.as_view(), name='blog'),
    path('blog/', cache_page(60)(BlogListView.as_view()), name='blog_list'),
    path('create_blog/', BlogCreateView.as_view(), name='blog_create'),
    path('update/<slug>', BlogUpdateView.as_view(), name='blog_update'),
    path('delete/<slug>', BlogDeleteView.as_view(), name='blog_delete'),
    path('published/<int:pk>', toggle_published, name='toggle_published')
]
