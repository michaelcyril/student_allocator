from django.urls import path
from .location import *
from .views import *

app_name = "app"
urlpatterns = [
    path('demo', InsertSchools),
]
