from django.shortcuts import render

from webapp.models import Item


def index_view(request, *args, **kwargs):
    items = Item.objects.all()
    return render(request, 'index.html',context={'items': items})
