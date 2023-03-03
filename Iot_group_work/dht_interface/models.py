from django.db import models

class Sensor_values(models.Model):
    temprature=models.IntegerField()
    humidity=models.IntegerField()
    time_red=models.DateTimeField(auto_now=True)

    

