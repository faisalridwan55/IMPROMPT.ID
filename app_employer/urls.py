from django.conf.urls import url
from .views import *
#url for app
urlpatterns = [
    url(r'^home/', home_employer, name='home-employer'),
    url(r'^edit_company_profile/', edit_company_profile, name='edit-company-profile'),
    url(r'^home/post/', opportunity_posting, name='opportunity-posting'),
]
