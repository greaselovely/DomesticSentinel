# main/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    VendorViewSet, VendorContactViewSet, TaskViewSet, InventoryViewSet,
    ProductViewSet, PurchaseRecordViewSet, ReminderViewSet, HouseProjectViewSet,
    VendorQuoteViewSet, WarrantyViewSet, MaintenanceTaskViewSet, DocumentViewSet,
    SmartHomeDeviceViewSet, EnergyUsageViewSet, ProductDetail
)
from .auth import CustomAuthToken

router = DefaultRouter()
router.register(r'vendors', VendorViewSet)
router.register(r'vendor-contacts', VendorContactViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'inventories', InventoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'purchase-records', PurchaseRecordViewSet)
router.register(r'reminders', ReminderViewSet)
router.register(r'house-projects', HouseProjectViewSet)
router.register(r'vendor-quotes', VendorQuoteViewSet)
router.register(r'warranties', WarrantyViewSet)
router.register(r'maintenance-tasks', MaintenanceTaskViewSet)
router.register(r'documents', DocumentViewSet)
router.register(r'smart-home-devices', SmartHomeDeviceViewSet)
router.register(r'energy-usage', EnergyUsageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', CustomAuthToken.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
]