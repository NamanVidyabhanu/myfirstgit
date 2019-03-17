# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Bid_desk(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=20)
    type1 = models.CharField(max_length=20)
    age = models.CharField(max_length=3)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
