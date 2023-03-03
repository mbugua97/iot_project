from django.shortcuts import render


def dht_homepage(request):
    return render(request,'dht_interface/index.html')

# Create your views here.
