from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    #photos = Photo.objects.all().order_by(get_order_photos(request))[:12]
    return render(
        request,
        'index_gal.html',
        #context={'photos': photos}
    )
