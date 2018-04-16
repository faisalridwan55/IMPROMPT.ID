from django.conf.urls import url
from .views import *
#url for app
urlpatterns = [
    url(r'^home/$', home_public, name='home-public'),
    url(r'^about/$', about_company, name='about-company'),
    url(r'^news/$', news_page, name='news-page'),
    url(r'^news/(?P<pk>\d)/$', news_detail, name='news-detail'),
    url(r'^opportunity/(?P<categories>\d)/$', opportunity_page, name='news-detail'),
    url(r'^opportunity/(?P<categories>\d)/(?P<pk>\d)/$', opportunity_detail, name='news-detail'),
    url(r'^search/$', search_by_drop_down, name='search-by-drop-down'),
]
