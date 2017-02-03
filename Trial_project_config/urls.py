"""Trial_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

from authentication import views as trial_auth_views
from Trial_app.forms import LoginForm

urlpatterns = [
    url(r'^trial/', include('Trial_app.urls')),
    url(r'^$', TemplateView.as_view(template_name='Trial_app/feeds.html'), name='feeds'),

    url(r'^login/$', auth_views.login, {
        'template_name' : 'Trial_app/login.html',
        'authentication_form' : LoginForm,
    }, name='login'),

    url(r'^logout/$', auth_views.logout, {'next_page' : 'login'}, name='logout'),
    url(r'^register/$', trial_auth_views.register, name='trial_register'),
    url(r'^admin/', admin.site.urls),
]
