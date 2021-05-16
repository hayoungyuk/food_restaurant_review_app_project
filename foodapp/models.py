from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django import forms

# Create your models here.
class Foodapp(models.Model):
    location = models.CharField(max_length=300)
    eater = models.CharField(max_length=150)
    date = models.DateTimeField()
    content = models.TextField()
    photos = models.ImageField(blank=True, upload_to = "foodapp/", null=True)
    photos_thumbnail = ImageSpecField(source = 'photos', processors =[ResizeToFill(120,120)])

    def __str__(self):
        return self.location

    def summary(self):
        return self.content[:6]

class FoodappForm(forms.ModelForm):
    class Meta:
        model = Foodapp
        fields = ['location', 'eater', 'content','photos']