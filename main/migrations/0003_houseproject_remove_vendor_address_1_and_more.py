# Generated by Django 5.0.6 on 2024-06-23 19:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_inventory_options_alter_purchaserecord_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('goals', models.TextField()),
                ('files_url', models.URLField()),
                ('estimated_budget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('planned', 'Planned'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ('on_hold', 'On Hold')], max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='address_1',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='address_2',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='business_card',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='city',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='email',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='state',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='zip_code',
        ),
        migrations.AddField(
            model_name='reminder',
            name='recurrence',
            field=models.CharField(blank=True, choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('yearly', 'Yearly')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('not_started', 'Not Started'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ('on_hold', 'On Hold'), ('cancelled', 'Cancelled')], max_length=20),
        ),
        migrations.CreateModel(
            name='VendorContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('address_1', models.CharField(max_length=100)),
                ('address_2', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
                ('zip_code', models.CharField(max_length=10)),
                ('business_card', models.ImageField(blank=True, null=True, upload_to='business_cards/')),
                ('is_primary', models.BooleanField(default=False)),
                ('contact_type', models.CharField(choices=[('sales', 'Sales'), ('support', 'Support'), ('billing', 'Billing'), ('other', 'Other')], default='other', max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('preferred_contact_method', models.CharField(choices=[('email', 'Email'), ('phone', 'Phone'), ('mail', 'Mail')], default='email', max_length=10)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='main.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='VendorQuote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote_number', models.CharField(max_length=50)),
                ('quote_date', models.DateField()),
                ('quote_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], max_length=20)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.houseproject')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.vendor')),
                ('vendor_contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.vendorcontact')),
            ],
        ),
    ]