# Generated by Django 4.1.7 on 2023-03-03 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dht_interface', '0002_sensor_values'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Sensor_Data',
        ),
    ]
