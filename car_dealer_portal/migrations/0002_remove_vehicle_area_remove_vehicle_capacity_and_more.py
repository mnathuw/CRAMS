# Generated by Django 5.1.3 on 2024-11-27 16:19

import ckeditor.fields
import datetime
import django.db.models.deletion
import multiselectfield.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_dealer_portal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='area',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='capacity',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='body_style',
            field=models.CharField(default='Sedan', max_length=100),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='car_photo',
            field=models.ImageField(default='photos/default.jpg', upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='car_photo_1',
            field=models.ImageField(blank=True, default='photos/default.jpg', upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='car_photo_2',
            field=models.ImageField(blank=True, default='photos/default.jpg', upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='car_photo_3',
            field=models.ImageField(blank=True, default='photos/default.jpg', upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='car_photo_4',
            field=models.ImageField(blank=True, default='photos/default.jpg', upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='city',
            field=models.CharField(default='Waterloo', max_length=100),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='condition',
            field=models.CharField(default='New', max_length=100),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='doors',
            field=models.CharField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='4', max_length=10),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='engine',
            field=models.CharField(default='2.0L', max_length=100),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='features',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Cruise Control', 'Cruise Control'), ('Audio Interface', 'Audio Interface'), ('Airbags', 'Airbags'), ('Air Conditioning', 'Air Conditioning'), ('Seat Heating', 'Seat Heating'), ('Alarm System', 'Alarm System'), ('ParkAssist', 'ParkAssist'), ('Power Steering', 'Power Steering'), ('Reversing Camera', 'Reversing Camera'), ('Direct Fuel Injection', 'Direct Fuel Injection'), ('Auto Start/Stop', 'Auto Start/Stop'), ('Wind Deflector', 'Wind Deflector'), ('Bluetooth Handset', 'Bluetooth Handset')], default=[], max_length=195),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='fuel_type',
            field=models.CharField(default='Gasoline', max_length=50),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='interior',
            field=models.CharField(default='Leather', max_length=100),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='milage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='miles',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='model',
            field=models.CharField(default='Default Model', max_length=100),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='passengers',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='province',
            field=models.CharField(choices=[('AB', 'Alberta'), ('BC', 'British Columbia'), ('MB', 'Manitoba'), ('NB', 'New Brunswick'), ('NL', 'Newfoundland and Labrador'), ('NS', 'Nova Scotia'), ('NT', 'Northwest Territories'), ('NU', 'Nunavut'), ('ON', 'Ontario'), ('PE', 'Prince Edward Island'), ('QC', 'Quebec'), ('SK', 'Saskatchewan'), ('YT', 'Yukon')], default='ON', max_length=100),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='transmission',
            field=models.CharField(default='Automatic', max_length=100),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vin_no',
            field=models.CharField(default='UNKNOWN', max_length=100),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='year',
            field=models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024)], default=2024, verbose_name='year'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='car_name',
            field=models.CharField(default='Generic Car Name', max_length=255),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='color',
            field=models.CharField(default='Black', max_length=100),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='dealer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='car_dealer_portal.cardealer'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='description',
            field=ckeditor.fields.RichTextField(default='No description available.'),
        ),
    ]
