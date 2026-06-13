from django.db import models

class SimpleInterest(models.Model):
    principal = models.IntegerField()
    rate = models.FloatField()
    time = models.FloatField()

    def __str__(self):
        return str(self.principal)