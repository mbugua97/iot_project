from django.shortcuts import render
from . models import Sensor_values
import Adafruit_DHT


pin = 4
sensor = Adafruit_DHT.DHT11
def dht_homepage(request):
    pin = 4
    sensor = Adafruit_DHT.DHT11
    hum, temp = Adafruit_DHT.read_retry(sensor, pin)
    if hum is not None and temp is not None:
        print(f'Temperature: {temp}')
        print(f'Humidity: {hum}')
    else:
        print('Failed to read sensor data')

    data=Sensor_values.objects.all()
    rsvd_data=Sensor_values(temprature=temp,humidity=hum)
    rsvd_data.save()
    context={'data':data}
    return render(request,'dht_interface/index.html',context)