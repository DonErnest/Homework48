from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest

from webapp.models import Item


def index_view(request, *args, **kwargs):
    items = Item.objects.filter(amount__gte=1).order_by('category', 'name')
    return render(request, 'index.html',context={'items': items})


def item_view(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'item_view.html', context={'item': item})



