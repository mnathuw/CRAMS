# Generated by Django 5.1.3 on 2024-11-18 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cars',
            field=models.CharField(default='', max_length=50),
        ),
    ]
