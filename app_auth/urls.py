from django.conf.urls import url
from .views import *
#url for app
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login/', login, name='login'),
    url(r'^test/', test, name='test'),
    url(r'^test1/', test1, name='test1'),
]
