from django.http import HttpResponse
from django.shortcuts import render

from site_shop.models import Section, Photo


def index(request):
    sections = Section.objects.all().order_by('title')
    photos = Photo.objects.all()[:12]
    return render(
        request,
        'index.html',
        context={'sections': sections,
                 'photos': photos}
    )


def test_view(request):
    return HttpResponse("Это тестовая страница")
