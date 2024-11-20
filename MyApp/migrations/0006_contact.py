# Generated by Django 5.1.3 on 2024-11-18 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0005_order_date_order_days_for_rent_order_loc_from_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150)),
                ('email', models.CharField(default='', max_length=150)),
                ('phone_number', models.CharField(default='', max_length=15)),
                ('message', models.TextField(default='', max_length=500)),
            ],
        ),
    ]