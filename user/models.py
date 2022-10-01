from django.db import models

# Create your models here.
class register(models.Model):
    ft_name=models.CharField(max_length=90)
    lt_name=models.CharField(max_length=90)
    mail=models.EmailField(max_length=90)
    pasd=models.CharField(max_length=90)

class yield_data(models.Model):
    crop=models.IntegerField()
    rain=models.IntegerField()
    pesticide=models.IntegerField()
    year=models.IntegerField()
    avg_temp=models.IntegerField()
