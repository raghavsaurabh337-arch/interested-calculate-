from django.db import models

# Create your models here.
class simple_interest(models.Model):
     principal=models.IntegerField(max_length=100)
     rate=models.FloatField(max_length=50)
     time=models.IntegerField(max_length=50)
