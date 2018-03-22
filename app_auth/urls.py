from django.conf.urls import url
from .views import *
#url for app
urlpatterns = [
    url(r'^$', index, name='index'),
]
