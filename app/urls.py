from django.urls import path
from .views import list_view

urlpatterns = [
    path('', list_view, name='property-list'),
    # path('properties/<int:pk>/', PropertyDetailView.as_view(), name='property-detail'),
]
