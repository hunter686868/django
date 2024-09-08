from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from site_shop.forms import SearchForm
from site_shop.models import Section, Photo


def index(request):
    photos = Photo.objects.all().order_by(get_order_photos(request))[:12]
    return render(
        request,
        'index.html',
        context={'photos': photos}
    )


def test_view(request):
    return HttpResponse("Это тестовая страница")


def get_order_photos(request):
    order_by = '-uploaded_at'

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


def search(request):
    search_form = SearchForm(request.GET)
    if search_form.is_valid():
        q = search_form.cleaned_data['q']
        photos = Photo.objects.filter(
            Q(title__icontains=q) | Q(description__icontains=q)
        )
        context = {'photos': photos, 'q': q}
        return render(
            request,
            'search.html',
            context=context
        )
