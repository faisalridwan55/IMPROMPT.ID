from django.conf.urls import url
from .views import *
#url for app
urlpatterns = [
    url(r'^$', login_page, name='login-page'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
]
