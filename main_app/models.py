from django.db import models
from main_app.validators import time_validator


class Recipe(models.Model):
    title = models.CharField(max_length=30)
    image_url = models.URLField(default='')
    description = models.TextField(default='')
    ingredients = models.CharField(max_length=250)
    time = models.IntegerField(validators=[time_validator])
