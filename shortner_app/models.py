from django.db import models

# Create your models here.
class Url_Model(models.Model):
    url = models.CharField(max_length=5000)
    short_url = models.CharField(max_length=10)