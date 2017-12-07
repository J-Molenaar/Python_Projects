from __future__ import unicode_literals

from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publish_date = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    in_print= models.BooleanField()
