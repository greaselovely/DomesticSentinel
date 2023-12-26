from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    unit = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    lot_size = models.DecimalField(max_digits=10, decimal_places=2)
    gas_provider = models.CharField(max_length=100, blank=True)
    electric_provider = models.CharField(max_length=100, blank=True)
    water_provider = models.CharField(max_length=100, blank=True)

class Vendor(models.Model):
    company_name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    unit = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

class Contact(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cell_phone = models.CharField(max_length=20, blank=True)
    desk_phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField()
    title = models.CharField(max_length=100, blank=True)
    manager_name = models.CharField(max_length=100, blank=True)
    booking_url = models.URLField(blank=True)
    business_card_front = models.ImageField(upload_to='business_cards/')
    business_card_back = models.ImageField(upload_to='business_cards/', blank=True)


class MaintenanceRecord(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date_work_performed = models.DateField()
    date_work_accepted_closed = models.DateField()
    notes = models.TextField()
    equipment_service_types = models.ManyToManyField('EquipmentType', blank=True)

class EquipmentType(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    equip_type_notes = models.TextField()


class Inventory(models.Model):
    item_name = models.CharField(max_length=100)
    first_purchase_date = models.DateField()
    urls = models.JSONField(default=list)
    tags = models.ManyToManyField('Tag', blank=True)
    product_image = models.ImageField(upload_to='inventory_images/', blank=True)
    barcode = models.CharField(max_length=100, blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=50)


class Projects(models.Model):
    PROJECT_STATUS_PLANNED = 'P'
    PROJECT_STATUS_IN_PROGRESS = 'I'
    PROJECT_STATUS_COMPLETED = 'C'
    
    PROJECT_STATUS_CHOICES = [
        (PROJECT_STATUS_PLANNED, 'Planning'),
        (PROJECT_STATUS_IN_PROGRESS, 'In Progress'),
        (PROJECT_STATUS_COMPLETED, 'Completed'),
    ]

    project_details = models.TextField()
    associated_vendors = models.ManyToManyField(Vendor, blank=True)
    status = models.CharField(max_length=10, choices=PROJECT_STATUS_CHOICES)
