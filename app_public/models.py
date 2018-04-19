from django.db import models

# Create your models here.
class Imprompt_Profile(models.Model):
	baris_atas_judul = models.CharField(max_length=140, blank=False)
	baris_atas_description = models.TextField(blank=False)
	baris_tengah_judul = models.CharField(max_length=140, blank=False)
	baris_tengah = models.TextField(blank=True)
	baris_bawah_judul = models.CharField(max_length=140, blank=False)
	baris_bawah = models.TextField(blank=True)

class News(models.Model):
    news_title = models.CharField(max_length=140, blank=False)
    news_short_description = models.CharField(max_length=140, blank=False)
    news_description = models.TextField(blank=False)
