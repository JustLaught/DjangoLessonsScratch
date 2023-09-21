from django.shortcuts import render
from .models import Page

# Create your views here.
def index(request, page_name):
    page_name = '/' + page_name
    pg = Page.objects.get(permalink=page_name)
    page_list = Page.objects.all()
    context = {
        'title': pg.title,
        'bodytext': pg.bodytext,
        'permalink': pg.permalink,
        'last_updated': pg.update_date,
        'page_list': page_list,
    }
    return render(request, 'index.html', context)