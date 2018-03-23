"""IMPROMPT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
import app_auth.urls as app_auth
import app_employer.urls as app_employer
import app_job_seeker.urls as app_job_seeker

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^public_home/', include(app_auth, namespace='app_auth')),
    url(r'^employer/', include(app_employer, namespace='app_employer')),
    url(r'^job_seeker/', include(app_job_seeker, namespace='app_job_seeker')),
    url(r'^$', RedirectView.as_view(permanent=True, url='/public_home/'), name='index'),
]
