# main/filters.py
from django_filters import rest_framework as filters
from .models import Vendor, Task, Reminder, Inventory, Product, PurchaseRecord, VendorContact

class VendorFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    category = filters.CharFilter(lookup_expr='icontains')
    last_service_date_after = filters.DateFilter(field_name='last_service_date', lookup_expr='gte')
    last_service_date_before = filters.DateFilter(field_name='last_service_date', lookup_expr='lte')
    is_active = filters.BooleanFilter()

    class Meta:
        model = Vendor
        fields = ['name', 'category', 'last_service_date', 'is_active']

class VendorContactFilter(filters.FilterSet):
    vendor = filters.ModelChoiceFilter(queryset=Vendor.objects.all())
    first_name = filters.CharFilter(lookup_expr='icontains')
    last_name = filters.CharFilter(lookup_expr='icontains')
    city = filters.CharFilter(lookup_expr='icontains')
    state = filters.CharFilter(lookup_expr='exact')
    is_primary = filters.BooleanFilter()
    contact_type = filters.ChoiceFilter(choices=VendorContact.CONTACT_TYPE_CHOICES)
    is_active = filters.BooleanFilter()

    class Meta:
        model = VendorContact
        fields = ['vendor', 'first_name', 'last_name', 'city', 'state', 'is_primary', 'contact_type', 'is_active']

class TaskFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    start_date_after = filters.DateFilter(field_name='start_date', lookup_expr='gte')
    start_date_before = filters.DateFilter(field_name='start_date', lookup_expr='lte')
    end_date_after = filters.DateFilter(field_name='end_date', lookup_expr='gte')
    end_date_before = filters.DateFilter(field_name='end_date', lookup_expr='lte')

    class Meta:
        model = Task
        fields = ['title', 'task_type', 'status', 'start_date', 'end_date']

class ReminderFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    due_date_after = filters.DateFilter(field_name='due_date', lookup_expr='gte')
    due_date_before = filters.DateFilter(field_name='due_date', lookup_expr='lte')

    class Meta:
        model = Reminder
        fields = ['title', 'is_recurring', 'due_date']

class InventoryFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    purchase_date_after = filters.DateFilter(field_name='purchase_date', lookup_expr='gte')
    purchase_date_before = filters.DateFilter(field_name='purchase_date', lookup_expr='lte')
    price_min = filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Inventory
        fields = ['name', 'manufacturer', 'purchase_date', 'price']

class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    manufacturer = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['name', 'manufacturer']

class PurchaseRecordFilter(filters.FilterSet):
    purchase_date_after = filters.DateFilter(field_name='purchase_date', lookup_expr='gte')
    purchase_date_before = filters.DateFilter(field_name='purchase_date', lookup_expr='lte')
    price_min = filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = PurchaseRecord
        fields = ['product', 'purchase_date', 'price', 'website']