# Generated by Django 4.1.7 on 2023-03-03 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temprature', models.IntegerField()),
                ('humidity', models.IntegerField()),
                ('time_red', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]