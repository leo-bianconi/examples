from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.contrib.auth.decorators import login_required

def market_index(request):
    items = Item.objects.all()
    return render(request, 'market/market_index.html', { 'items': items })

def item_details(request, slug):
    item = Item.objects.get(slug=slug)
    return render(request, 'market/item_details.html', { 'item': item })

@login_required(login_url='/accounts/login')
def sell_view(request):
    return render(request, 'market/sell.html')
