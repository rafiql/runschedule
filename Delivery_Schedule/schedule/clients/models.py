from django.db import models
from django.urls import reverse

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    mobile = models.CharField(max_length=256)
    address = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home")
