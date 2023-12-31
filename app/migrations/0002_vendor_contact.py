# Generated by Django 5.0 on 2023-12-26 21:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('unit', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('cell_phone', models.CharField(blank=True, max_length=20)),
                ('desk_phone', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('manager_name', models.CharField(blank=True, max_length=100)),
                ('booking_url', models.URLField(blank=True)),
                ('business_card_front', models.ImageField(upload_to='business_cards/')),
                ('business_card_back', models.ImageField(blank=True, upload_to='business_cards/')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.vendor')),
            ],
        ),
    ]
