# Generated by Django 5.1 on 2024-09-01 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockpredictor', '0005_stockdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockdata',
            name='end',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='start',
            field=models.TextField(null=True),
        ),
        migrations.DeleteModel(
            name='StockHistory',
        ),
    ]
