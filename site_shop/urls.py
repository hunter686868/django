from django.urls import path, include

urlpatterns = [
    path("", include('site_shop.urls')),
]