from django.contrib import admin
from .models import *
# Register your models here.

a = [User,Mkoa, Wilaya, Kata, QuantityRequired, School, Student, StudentSchool]
for i in a:
    admin.site.register(i)
