# Generated by Django 5.1 on 2024-09-01 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockpredictor', '0006_stockdata_end_stockdata_start_delete_stockhistory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockdata',
            name='end',
        ),
        migrations.RemoveField(
            model_name='stockdata',
            name='start',
        ),
    ]
