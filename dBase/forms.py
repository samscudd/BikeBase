from django import forms
from django.core.exceptions import ValidationError
from .models import Bikes, Wheels



class BikesForm(forms.Form):
    manufacturer = forms.CharField(label='Bike Manufacturer', max_length=20)
    bike_model = forms.CharField(label='Bike Model', max_length=20)
    wheel_size = forms.DecimalField(label='Wheel Size', max_digits=4, decimal_places=1)
    brakes_mounts = forms.CharField(label='Brake Mounts', max_length=20)

class WheelsForm(forms.Form):