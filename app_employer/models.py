from django.db import models

# Create your models here.
class Employer(models.Model):
    profile_id = models.CharField(max_length=140, blank=False)
    name = models.CharField(max_length=140, blank=False)
    email = models.CharField(max_length=140, blank=False)
