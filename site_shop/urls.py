from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delivery', views.delivery, name='delivery'),
    path('search', views.search, name='search'),
]
