from django.urls import path
from .location import *

app_name = "app"
urlpatterns = [
    path('demo', MkoaWilayaKata),
]
