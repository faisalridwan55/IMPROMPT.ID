from django.conf.urls import url
from .views import *
#url for app
urlpatterns = [
    url(r'^home/', home_job_seeker, name='home-job-seeker'),
    url(r'^edit_profile/', edit_profile, name='edit-profile'),
    url(r'^edit_profile/submit/', submit_job_seeker_profile, name='submit-job-seeker-profile'),
]
