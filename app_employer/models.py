from django.db import models

# Create your models here.
class Employer(models.Model):
    profile_id = models.CharField(max_length=140, blank=False)
    first_name = models.CharField(max_length=140, blank=False)
    last_name = models.CharField(max_length=140, blank=False)
    email = models.CharField(max_length=140, blank=False)
    phone_number = models.CharField(max_length=20, blank=True)

class Company(models.Model):
    company_creator_profile_id = models.CharField(max_length=140, blank=False)
    country = models.CharField(max_length=140, blank=False)
    province = models.CharField(max_length=140, blank=False)
    city = models.CharField(max_length=140, blank=False)
    company_name = models.CharField(max_length=140, blank=False)
    company_description = models.TextField(blank=False)
    company_website = models.CharField(max_length=140, blank=False)
    company_logo = models.FileField(upload_to='company_logo/')
