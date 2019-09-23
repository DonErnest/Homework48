from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest

from webapp.forms import SearchForm
from webapp.models import Item
import re

def index_view(request, *args, **kwargs):
    items = Item.objects.filter(amount__gte=1).order_by('category', 'name')
    search = SearchForm()
    return render(request, 'index.html',context={'items': items, 'search': search})


def item_view(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'item_view.html', context={'item': item})


def search_view(request, *args, **kwargs):
    search = SearchForm(data=request.GET)
    if search.is_valid():
        text=search.cleaned_data['search_text']
        if bool(re.search('[\u0400-\u04FF]', text)):
            items = Item.objects.all()
            rus_items=[]
            for item in items:
                if text.lower() in item.name.lower():
                    rus_items.append(item)
            items = rus_items
            return render(request, 'search_results.html', context={'items': items, 'text': text})
        else:
            items = Item.objects.filter(name__icontains=text.lower())
            return render(request, 'search_results.html', context={'items': items, 'text': text})
    else:
        return render(request, 'search_results.html', context={'text': None})




