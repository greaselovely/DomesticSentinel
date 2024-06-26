# Generated by Django 5.0.6 on 2024-06-23 17:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField(default=1)),
                ('purchase_date', models.DateField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('manufacturer', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('manufacturer', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('due_date', models.DateField()),
                ('is_recurring', models.BooleanField(default=False)),
                ('recurrence_interval', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact_info', models.TextField()),
                ('business_card', models.ImageField(blank=True, null=True, upload_to='business_cards/')),
                ('last_service_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('purchase_date', models.DateField()),
                ('website', models.URLField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('task_type', models.CharField(choices=[('MAINTENANCE', 'Maintenance'), ('PROJECT', 'Project'), ('SEASONAL', 'Seasonal')], max_length=20)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(max_length=20)),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.vendor')),
            ],
        ),
    ]
