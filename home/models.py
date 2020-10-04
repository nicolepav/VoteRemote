from django.db import models

# Create your models here.
class state_key(models.Model):

    name = models.CharField(max_length = 40)
    abbreviation = models.CharField(max_length=3)

