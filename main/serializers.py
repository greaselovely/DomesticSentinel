# main/serializers.py
from rest_framework import serializers
from .models import (
    Vendor, VendorContact, Task, Inventory, Product, PurchaseRecord, Reminder,
    HouseProject, VendorQuote, Warranty, MaintenanceTask, Document, SmartHomeDevice, EnergyUsage
)

# Keep your existing serializers as they are

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class VendorContactSerializer(serializers.ModelSerializer):
    vendor_name = serializers.CharField(source='vendor.name', read_only=True)
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = VendorContact
        fields = '__all__'
    
    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

class VendorWithContactsSerializer(serializers.ModelSerializer):
    contacts = VendorContactSerializer(many=True, read_only=True)

    class Meta:
        model = Vendor
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    vendor_name = serializers.CharField(source='vendor.name', read_only=True)

    class Meta:
        model = Task
        fields = '__all__'

    def validate_end_date(self, value):
        if value and value < self.initial_data.get('start_date'):
            raise serializers.ValidationError("End date must be after start date.")
        return value

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    purchase_history = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_purchase_history(self, obj):
        purchase_records = PurchaseRecord.objects.filter(product=obj).order_by('-purchase_date')
        return PurchaseRecordSerializer(purchase_records, many=True).data

class PurchaseRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseRecord
        fields = '__all__'

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = '__all__'

# Add new serializers for the new models

class HouseProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseProject
        fields = '__all__'

class VendorQuoteSerializer(serializers.ModelSerializer):
    vendor_name = serializers.CharField(source='vendor.name', read_only=True)
    contact_name = serializers.CharField(source='vendor_contact.get_full_name', read_only=True)

    class Meta:
        model = VendorQuote
        fields = '__all__'

class WarrantySerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    vendor_name = serializers.CharField(source='vendor.name', read_only=True)

    class Meta:
        model = Warranty
        fields = '__all__'

class MaintenanceTaskSerializer(serializers.ModelSerializer):
    associated_item_name = serializers.CharField(source='associated_item.name', read_only=True)

    class Meta:
        model = MaintenanceTask
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    related_project_name = serializers.CharField(source='related_project.name', read_only=True)
    related_purchase_product = serializers.CharField(source='related_purchase.product.name', read_only=True)

    class Meta:
        model = Document
        fields = '__all__'

class SmartHomeDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartHomeDevice
        fields = '__all__'

class EnergyUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnergyUsage
        fields = '__all__'