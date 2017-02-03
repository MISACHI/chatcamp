from django.conf.urls import url
from Trial_app.views import index, home, profile, feeds, message

urlpatterns = [
    url(r'^$', index, name='trial_index'),
    url(r'^home/$', home, name='trial_home'),
    url(r'^feeds/$', feeds, name='trial_feeds'),
    # url(r'^signup/$', register, name='trial_signup'),
    url(r'^profile/$', profile, name='trial_profile'),
    url(r'^message/$', message, name='trial_message'),
]