# main/views.py
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django.core.exceptions import ValidationError
from rest_framework.exceptions import ValidationError as DRFValidationError
from .filters import (
    VendorFilter, VendorContactFilter, TaskFilter, ReminderFilter, 
    InventoryFilter, ProductFilter, PurchaseRecordFilter
)
from .models import (
    Vendor, VendorContact, Task, Inventory, Product, PurchaseRecord, Reminder,
    HouseProject, VendorQuote, Warranty, MaintenanceTask, Document, SmartHomeDevice, EnergyUsage
)
from .serializers import (
    VendorSerializer, VendorContactSerializer, TaskSerializer, InventorySerializer,
    ProductSerializer, PurchaseRecordSerializer, ReminderSerializer, HouseProjectSerializer,
    VendorQuoteSerializer, WarrantySerializer, MaintenanceTaskSerializer, DocumentSerializer,
    SmartHomeDeviceSerializer, EnergyUsageSerializer
)
import logging

logger = logging.getLogger(__name__)

class BaseModelViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except (ValidationError, DRFValidationError) as e:
            logger.error(f"Validation error in {self.__class__.__name__}: {str(e)}")
            if isinstance(e, DRFValidationError):
                error_dict = e.get_full_details()
                date_fields = [
                    'last_service_date_after', 'last_service_date_before',
                    'start_date_after', 'start_date_before',
                    'end_date_after', 'end_date_before',
                    'due_date_after', 'due_date_before',
                    'purchase_date_after', 'purchase_date_before'
                ]
                for field in date_fields:
                    if field in error_dict:
                        return Response(
                            {"error": f"Invalid date format for {field}. Please use YYYY-MM-DD format."},
                            status=status.HTTP_400_BAD_REQUEST
                        )
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Unexpected error in {self.__class__.__name__}: {str(e)}")
            return Response({"error": "An unexpected error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class VendorViewSet(BaseModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    filterset_class = VendorFilter
    search_fields = ['name', 'category']
    ordering_fields = ['name', 'last_service_date']

class VendorContactViewSet(BaseModelViewSet):
    queryset = VendorContact.objects.all()
    serializer_class = VendorContactSerializer
    filterset_class = VendorContactFilter
    search_fields = ['first_name', 'last_name', 'email']
    ordering_fields = ['first_name', 'last_name', 'vendor__name']

class TaskViewSet(BaseModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filterset_class = TaskFilter
    search_fields = ['title', 'description']
    ordering_fields = ['start_date', 'end_date']

class InventoryViewSet(BaseModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    filterset_class = InventoryFilter
    search_fields = ['name', 'description', 'manufacturer']
    ordering_fields = ['name', 'purchase_date', 'price']

class ProductViewSet(BaseModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    search_fields = ['name', 'description', 'manufacturer']
    ordering_fields = ['name']

class PurchaseRecordViewSet(BaseModelViewSet):
    queryset = PurchaseRecord.objects.all()
    serializer_class = PurchaseRecordSerializer
    filterset_class = PurchaseRecordFilter
    search_fields = ['product__name', 'website']
    ordering_fields = ['purchase_date', 'price']

class ReminderViewSet(BaseModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
    filterset_class = ReminderFilter
    search_fields = ['title', 'description']
    ordering_fields = ['due_date']

class HouseProjectViewSet(BaseModelViewSet):
    queryset = HouseProject.objects.all()
    serializer_class = HouseProjectSerializer
    search_fields = ['name', 'goals']
    ordering_fields = ['start_date', 'end_date', 'estimated_budget']

class VendorQuoteViewSet(BaseModelViewSet):
    queryset = VendorQuote.objects.all()
    serializer_class = VendorQuoteSerializer
    search_fields = ['vendor__name', 'project__name', 'quote_number']
    ordering_fields = ['quote_date', 'quote_amount']

class WarrantyViewSet(BaseModelViewSet):
    queryset = Warranty.objects.all()
    serializer_class = WarrantySerializer
    search_fields = ['product__name', 'vendor__name', 'description']
    ordering_fields = ['start_date', 'end_date']

class MaintenanceTaskViewSet(BaseModelViewSet):
    queryset = MaintenanceTask.objects.all()
    serializer_class = MaintenanceTaskSerializer
    search_fields = ['name', 'description']
    ordering_fields = ['next_due', 'last_performed']

class DocumentViewSet(BaseModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    search_fields = ['title', 'category']
    ordering_fields = ['upload_date']

class SmartHomeDeviceViewSet(BaseModelViewSet):
    queryset = SmartHomeDevice.objects.all()
    serializer_class = SmartHomeDeviceSerializer
    search_fields = ['name', 'device_type']
    ordering_fields = ['name', 'last_updated']

class EnergyUsageViewSet(BaseModelViewSet):
    queryset = EnergyUsage.objects.all()
    serializer_class = EnergyUsageSerializer
    search_fields = ['notes']
    ordering_fields = ['date', 'electricity_kwh', 'gas_therms', 'water_gallons']

class ProductDetail(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer