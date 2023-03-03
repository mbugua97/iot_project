from django.shortcuts import render
from . models import Sensor_values


def dht_homepage(request):
    data=Sensor_values.objects.all()
    context={'data':data}
    return render(request,'dht_interface/index.html',context)

# Create your views here.
