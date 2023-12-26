from django.views.generic import ListView, DetailView
from .models import Property

class PropertyListView(ListView):
    model = Property
    template_name = 'property_list.html'

class PropertyDetailView(DetailView):
    model = Property
    template_name = 'property_detail.html'  # Define your template path
