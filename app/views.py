from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.conf import settings

import os

from .models import Property

# def list_view(request):
#     items = Property.objects.all()
#     maps_url = "https://www.google.com/maps/place/"
#     context = {'items': items, 'maps_url': maps_url}
#     return render(request, 'property_list.html', context)

def list_view(request):
    items = Property.objects.all()
    for item in items:
        item.maps_address = "https://www.google.com/maps/place/" + '+'.join([
            item.street,
            item.city,
            item.state,
            item.zip_code
        ]).replace(' ', '+')
    context = {'items': items}
    return render(request, 'property_list.html', context)
