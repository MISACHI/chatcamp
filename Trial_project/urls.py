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
from django.conf import settings
from django.conf.urls.static import static

from authentication import views as trial_auth_views
from user_profile import views as trial_profile_views
from user_messages import views as trial_messages
from Trial_app.forms import LoginForm

urlpatterns = [
    url(r'^trial/', include('Trial_app.urls')),
    url(r'^$', TemplateView.as_view(template_name='feeds/feeds.html'), name='feeds'),

    url(r'^login/$', auth_views.login, {
        'template_name': 'Trial_app/login.html',
        'authentication_form': LoginForm,
    }, name='login'),

    url(r'^logout/$', auth_views.logout,
        {'next_page': 'login'},
        name='logout'),

    url(r'^register/', trial_auth_views.register, name='trial_signup'),
    url(r'^profile/', trial_profile_views.profile, name='trial_profile'),
    url(r'^feeds/', include('feeds.urls')),
    url(r'^messages/', include("user_messages.urls")),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
