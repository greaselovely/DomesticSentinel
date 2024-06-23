# main/models.py
from django.db import models
from django.contrib.auth.models import User

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=100, blank=True, null=True)
    address_2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    last_service_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class VendorContact(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='contacts')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    title = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    address_1 = models.CharField(max_length=100, blank=True, null=True)
    address_2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    business_card = models.ImageField(upload_to='business_cards/', null=True, blank=True)
    is_primary = models.BooleanField(default=False)
    CONTACT_TYPE_CHOICES = [
        ('sales', 'Sales'),
        ('support', 'Support'),
        ('billing', 'Billing'),
        ('other', 'Other'),
    ]
    contact_type = models.CharField(max_length=20, choices=CONTACT_TYPE_CHOICES, default='other')
    is_active = models.BooleanField(default=True)
    PREFERRED_CONTACT_CHOICES = [
        ('email', 'Email'),
        ('phone', 'Phone'),
        ('mail', 'Mail'),
    ]

    preferred_contact_method = models.CharField(max_length=10, choices=PREFERRED_CONTACT_CHOICES, default='email')

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.vendor.name}"
    
    class Meta:
        verbose_name_plural = "Vendor Contacts"

class Task(models.Model):
    TASK_TYPES = [
        ('MAINTENANCE', 'Maintenance'),
        ('PROJECT', 'Project'),
        ('SEASONAL', 'Seasonal'),
    ]
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    task_type = models.CharField(max_length=20, choices=TASK_TYPES)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, blank=True)

    STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('on_hold', 'On Hold'),
        ('cancelled', 'Cancelled'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title

class Inventory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField(default=1)
    url = models.URLField(blank=True, null=True)
    purchase_date = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    manufacturer = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Inventories"

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    manufacturer = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name

class PurchaseRecord(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateField()
    website = models.URLField()

    def __str__(self):
        return f"{self.product.name} - {self.purchase_date}"
    
    class Meta:
        verbose_name_plural = "Purchase History"

class Reminder(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    is_recurring = models.BooleanField(default=False)
    recurrence_interval = models.IntegerField(null=True, blank=True)

    RECURRENCE_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
    ]

    recurrence = models.CharField(max_length=10, choices=RECURRENCE_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.title

class HouseProject(models.Model):
    name = models.CharField(max_length=200)
    goals = models.TextField()
    files_url = models.URLField()
    estimated_budget = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[('planned', 'Planned'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ('on_hold', 'On Hold')])

class VendorQuote(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    vendor_contact = models.ForeignKey(VendorContact, on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(HouseProject, on_delete=models.CASCADE)
    quote_number = models.CharField(max_length=50)
    quote_date = models.DateField()
    quote_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')])

class Warranty(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='warranties')
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, related_name='warranties')
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    document = models.FileField(upload_to='warranty_docs/', null=True, blank=True)

    def __str__(self):
        return f"Warranty for {self.product.name} - Expires: {self.end_date}"



class MaintenanceTask(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    frequency = models.CharField(max_length=50, choices=[
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('annually', 'Annually'),
    ])
    last_performed = models.DateField(null=True, blank=True)
    next_due = models.DateField()
    associated_item = models.ForeignKey(Inventory, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - Next due: {self.next_due}"
    

class Document(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='documents/')
    upload_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100, choices=[
        ('house', 'House'),
        ('project', 'Project'),
        ('purchase', 'Purchase'),
        ('other', 'Other'),
    ])
    related_project = models.ForeignKey('HouseProject', on_delete=models.SET_NULL, null=True, blank=True)
    related_purchase = models.ForeignKey(PurchaseRecord, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
    
class SmartHomeDevice(models.Model):
    name = models.CharField(max_length=200)
    device_type = models.CharField(max_length=100)
    api_key = models.CharField(max_length=200)
    last_reading = models.JSONField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class EnergyUsage(models.Model):
    date = models.DateField()
    electricity_kwh = models.DecimalField(max_digits=10, decimal_places=2)
    gas_therms = models.DecimalField(max_digits=10, decimal_places=2)
    water_gallons = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Energy Usage on {self.date}"





# We'll implement tagging using a third-party package later