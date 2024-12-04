from django.db import models

class Register(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    block = models.CharField(max_length=5)
    apartment = models.IntegerField()

    def __str__(self):
        building = f"{self.block}{self.apartment}"
        return building