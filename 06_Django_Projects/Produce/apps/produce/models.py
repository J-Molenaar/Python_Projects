from __future__ import unicode_literals

from django.db import models

class Produce(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=255)
    weight = models.IntegerField()
    price = models.IntegerField()
    cost = models.FloatField()
    category = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
