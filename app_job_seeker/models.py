from django.db import models
from app_employer.models import Opportunity
from django.utils import timezone

# Create your models here.
class Job_Seeker(models.Model):
    profile_id = models.CharField(max_length=140, blank=False)
    profile_picture = models.ImageField()
    first_name = models.CharField(max_length=140, blank=False)
    last_name = models.CharField(max_length=140, blank=False)
    email = models.CharField(max_length=140, blank=False)
    phone_number = models.CharField(max_length=20, blank=True)
    birthday = models.DateTimeField(blank=True)
    resume = models.FileField()

class Application_Form(models.Model):
    job_seeker = models.ForeignKey(Job_Seeker,on_delete=models.CASCADE)
    opportunity = models.ForeignKey(Opportunity,on_delete=models.CASCADE)
