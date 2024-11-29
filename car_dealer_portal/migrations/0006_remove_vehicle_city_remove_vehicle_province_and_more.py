# Generated by Django 5.1.3 on 2024-11-28 18:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_dealer_portal', '0005_alter_vehicle_province'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='city',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='province',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='vehicles', to='car_dealer_portal.area'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='car_name',
            field=models.CharField(default='BMW', max_length=255),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='model',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vin_no',
            field=models.CharField(default='11111111111', max_length=100),
        ),
    ]