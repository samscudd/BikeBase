from django.contrib import admin

# Register your models here.
from .models import Bikes, Wheels

admin.site.register(Bikes)
admin.site.register(Wheels)