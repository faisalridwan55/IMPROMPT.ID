from django.conf.urls import url
from .views import *
#url for app
urlpatterns = [
    url(r'^home/', home, name='home'),
    url(r'^edit_company_profile/', edit_company_profile, name='edit_company_profile'),
]
