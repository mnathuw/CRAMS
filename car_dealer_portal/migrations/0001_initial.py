# Generated by Django 5.1.3 on 2024-11-26 01:44

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(default='Unknown', max_length=100)),
                ('city', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CarDealer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=13, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(13)])),
                ('wallet', models.IntegerField(default=0)),
                ('area', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='car_dealer_portal.area')),
                ('car_dealer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=10)),
                ('capacity', models.CharField(max_length=2)),
                ('is_available', models.BooleanField(default=True)),
                ('description', models.CharField(max_length=100)),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='car_dealer_portal.area')),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='car_dealer_portal.cardealer')),
            ],
        ),
    ]