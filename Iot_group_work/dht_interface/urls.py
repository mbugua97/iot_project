from django.urls import path
from . import views

urlpatterns=[
    path('',views.dht_homepage,name="dht")
]