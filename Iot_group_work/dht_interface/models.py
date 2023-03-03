from django.db import models

class Sensor_Data(models.Model):
    temprature=models.IntegerField()
    humidity=models.IntegerField()

    def __str__(self):
        return self.temprature

