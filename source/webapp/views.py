from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import SearchForm, ItemForm
from webapp.models import Item, category_choices
from re import search as re_search


def index_view(request, *args, **kwargs):
    items = Item.objects.filter(amount__gte=1).order_by('category', 'name')
    search = SearchForm()
    categories = category_choices
    return render(request, 'index.html',context={'items': items, 'search': search, 'categories': categories})


def item_view(request, pk):
    item = get_object_or_404(Item, pk=pk)
    search = SearchForm()
    categories = category_choices
    return render(request, 'item_view.html', context={'item': item, 'search': search, 'categories': categories})


def search_view(request, *args, **kwargs):
    search = SearchForm(data=request.GET)
    if search.is_valid():
        text=search.cleaned_data['search_text']
        if bool(re_search('[\u0400-\u04FF]', text)):
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


def add_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = ItemForm()
        return render(request, 'add.html', context={'form': form})
    elif request.method == 'POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            category = form.cleaned_data['category']
            amount = form.cleaned_data['amount']
            price = form.cleaned_data['price']
            item = Item.objects.create(name=name, description=description, category=category, amount=amount, price=price)
            return redirect('item_view', pk=item.pk)
        return render(request, 'add.html', context={'form': form})


def update_view(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'GET':
        form = ItemForm(data={'name': item.name, 'description': item.description,
                              'category': item.category, 'amount': item.amount, 'price': item.price})
        return render(request, 'update.html', context={'form': form, 'item': item})
    elif request.method == 'POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            item.name = form.cleaned_data['name']
            item.description = form.cleaned_data['description']
            item.category = form.cleaned_data['category']
            item.amount = form.cleaned_data['amount']
            item.price = form.cleaned_data['price']
            item.save()
            return redirect('item_view', pk=item.pk)
        else:
            return render(request, 'update.html', context={'form': form, 'item': item})


def delete(request,pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'item':item})
    elif request.method == 'POST':
        item.delete()
    return redirect('main')


def category_view(request, category):
    items = Item.objects.filter(category=category, amount__gte=1).order_by('name')
    categories = category_choices
    for option in categories:
        if option[0] == category:
            category_tuple = option
            break
    search = SearchForm()
    return render(request, 'by_category.html', context={'items': items, 'search': search, 'categories': categories, 'category': category_tuple})