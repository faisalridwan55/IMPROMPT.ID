from django.conf.urls import url
from .views import *
#url for app
urlpatterns = [
    url(r'^home/$', home_employer, name='home-employer'),
    url(r'^edit_company_profile/$', edit_company_profile, name='edit-company-profile'),
    url(r'^edit_employer_profile/$', edit_employer_profile, name='edit-employer-profile'),
    url(r'^company_profile/$', my_company_profile, name='company-profile'),
    url(r'^employer_profile/$', employer_profile, name='employer-profile'),
    url(r'^home/post/$', submit_opportunity_posting, name='opportunity-posting'),
    url(r'^edit_company_profile/submit/$', submit_company_profile, name='submit-company-profile'),
    url(r'^edit_employer_profile/submit/$', submit_employer_profile, name='submit-employer-profile'),

]
