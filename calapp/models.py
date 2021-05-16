from django.db import models

# Create your models here.

class Calapp(models.Model):
    body = models.CharField(max_length=100)
    photos = models.ImageField(blank=True, upload_to = "calapp/", null=True)