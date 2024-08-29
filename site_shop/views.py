from django.http import HttpResponse
from django.shortcuts import render

from site_shop.models import Section, Photo


def index(request):
    sections = Section.objects.all().order_by('title')
    photos = Photo.objects.all().order_by(get_order_photos(request))[:12]
    return render(
        request,
        'index.html',
        context={'sections': sections,
                 'photos': photos}
    )


def test_view(request):
    return HttpResponse("Это тестовая страница")


def get_order_photos(request):
    order_by = '-uploaded_at'  # Default ordering

    sort = request.GET.get('sort')
    up = request.GET.get('up')

    if sort == 'title':
        order_by = 'title' if up == '1' else '-title'

    return order_by

def delivery(request):
    return render(
        request,
        'delivery.html'
    )