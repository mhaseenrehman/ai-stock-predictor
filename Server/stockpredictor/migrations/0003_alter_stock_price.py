# Generated by Django 5.1 on 2024-08-29 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockpredictor', '0002_alter_stock_options_remove_stock_active_stock_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='price',
            field=models.DecimalField(decimal_places=100, max_digits=1000),
        ),
    ]
