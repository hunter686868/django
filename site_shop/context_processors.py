from site_shop.forms import SearchForm
from site_shop.models import Section


def add_data(request):
    sections = Section.objects.all().order_by('title')
    search_form = SearchForm()
    return {'sections': sections,
            'search_form': search_form}
