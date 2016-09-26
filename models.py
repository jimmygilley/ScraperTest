from django.db import models

# Create your models here.

class Odds(models.Model):
    favorite = models.CharField(max_length=200)
    spread = models.IntegerField(default=0)
    underdog = models.CharField(max_length=200)
    total = models.IntegerField(default=0)