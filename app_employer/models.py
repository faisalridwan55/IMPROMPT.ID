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

class Opportunity(models.Model):
    opportunity_category = models.CharField(max_length=140, blank=False)
    opportunity_field = models.CharField(max_length=140, blank=False)
    durations = models.CharField(max_length=140, blank=False)
    salary = models.CharField(max_length=140, blank=False)
    participants_needed = models.CharField(max_length=140, blank=False)
    requirements = models.TextField(blank=False)
    description = models.TextField(blank=False)
    contact_person_phone_number = models.CharField(max_length=140, blank=False)
    opportunity_owner = models.ForeignKey('Company')
