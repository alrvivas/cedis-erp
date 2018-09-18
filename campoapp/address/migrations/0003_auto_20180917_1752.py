# Generated by Django 2.1 on 2018-09-17 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_auto_20180820_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='lon',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=15, null=True),
        ),
    ]