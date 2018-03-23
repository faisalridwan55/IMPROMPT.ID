from django.conf.urls import url
from .views import *
#url for app
urlpatterns = [
    url(r'^home/', home, name='home'),
]
