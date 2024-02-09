from django.urls import path

from catalog.views import home, contact, catalog

urlpatterns = [
    path('', home),
    path('contact/', contact),
    path('catalog/', catalog)
]
