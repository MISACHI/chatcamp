from django.conf.urls import url
from feeds.views import post_feeds, feeds


urlpatterns = [
    url(r'^$', feeds, name='trial_feeds'),
    url(r'^post/$', post_feeds, name='trial_post_feeds'),
]
