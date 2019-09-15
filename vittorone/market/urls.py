from django.urls import path
from . import views

app_name = 'market'

urlpatterns = [
    path('', views.market_index, name='index'),
    path('item/<slug:slug>', views.item_details, name='item_details')
]
