from django.db import models

# Create your models here.
class Foodapp(models.Model):
    location = models.CharField(max_length=300)
    eater = models.CharField(max_length=150)
    date = models.DateTimeField()
    content = models.TextField()
    photos = models.ImageField(blank=True, upload_to = "foodapp/", null=True)

    def __str__(self):
        return self.location

    def summary(self):
        return self.content[:6]