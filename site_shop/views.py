from django.http import HttpResponse
from django.shortcuts import render

from site_shop.models import Section


def index(request):
    sections = Section.objects.all().order_by('title')
    return render(
        request,
        'index.html',
        context={'sections': sections}
    )


def test_view(request):
    return HttpResponse("Это тестовая страница")
