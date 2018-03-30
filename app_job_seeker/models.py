from django.db import models
from app_employer.models import Opportunity

# Create your models here.
class Job_Seeker(models.Model):
    profile_id = models.CharField(max_length=140, blank=False)
    first_name = models.CharField(max_length=140, blank=False)
    last_name = models.CharField(max_length=140, blank=False)
    email = models.CharField(max_length=140, blank=False)
    phone_number = models.CharField(max_length=20, blank=True)
    birthday = models.DateTimeField(blank=True)

class Application_Form(models.Model):
    job_seeker = models.ForeignKey('Job_Seeker')
    opportunity = models.ForeignKey('app_employer.Opportunity')
