# Generated by Django 5.0.6 on 2024-06-23 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_product_price_product_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
