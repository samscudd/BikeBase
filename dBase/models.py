from django.db import models

class Bikes(models.Model):
    manufacturer = models.CharField(max_length=20)
    bike_model = models.CharField(max_length=20)
    wheel_size = models.DecimalField(max_digits=4, decimal_places=1, choices=((29, "29"), (700, "700"), (27.5, "27.5")))
    brakes_mounts = models.CharField(max_length=20, choices=(("disc", "Disc"), ("rim", "Rim")))

    def __str__(self):
        return self.bike_model


class Wheels(models.Model):
    manufacturer = models.CharField(max_length=20)
    wheel_model = models.CharField(max_length=20) 
    size = models.DecimalField(max_digits=3, decimal_places=1, choices=((29, "29"), (700, "700"), (27.5, "27.5")))
    brakes = models.CharField(max_length=20, choices=(("disc", "Disc"), ("rim", "Rim")))
    front = models.BooleanField(default=True)
    back = models.BooleanField(default=True)

    def __str__(self):
        return self.wheel_model



