from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

def market_index(request):
    items = Item.objects.all()
    return render(request, 'market/market_index.html', { 'items': items })

def item_details(request, slug):
    item = Item.objects.get(slug=slug)
    return render(request, 'market/item_details.html', { 'item': item })
