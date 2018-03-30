from django.db import models

# Create your models here.
class Imprompt_Profile(models.Model):
    baris_atas = models.TextField(blank=False)
    baris_bawah = models.TextField(blank=True)
    active = models.BooleanField(default=False, unique=True)

class News(models.Model):
    news_short_description = models.CharField(max_length=140, blank=False)
    news_description = models.TextField(blank=False)
