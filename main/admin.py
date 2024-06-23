# main/admin.py
from django.contrib import admin
from .models import Vendor, Task, Inventory, Product, PurchaseRecord, Reminder, VendorContact

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_active', 'last_service_date')
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'category')

@admin.register(VendorContact)
class VendorContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'vendor', 'title', 'email', 'is_primary', 'is_active')
    list_filter = ('vendor', 'is_primary', 'is_active', 'contact_type')
    search_fields = ('first_name', 'last_name', 'email', 'vendor__name')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'task_type', 'start_date', 'end_date', 'status')
    list_filter = ('task_type', 'status')
    search_fields = ('title', 'description')

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'purchase_date', 'price')
    search_fields = ('name', 'description', 'manufacturer')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer')
    search_fields = ('name', 'description', 'manufacturer')

@admin.register(PurchaseRecord)
class PurchaseRecordAdmin(admin.ModelAdmin):
    list_display = ('product', 'price', 'purchase_date', 'website')
    list_filter = ('purchase_date',)
    search_fields = ('product__name', 'website')

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'is_recurring')
    list_filter = ('is_recurring',)
    search_fields = ('title', 'description')