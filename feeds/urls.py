from django.conf.urls import url
from feeds import views


urlpatterns = [
    url(r'^$', views.feeds, name='trial_feeds'),
    url(r'^post/$', views.post_feeds, name='trial_post_feeds'),
    url(r'^save_comments/$', views.comment, name='save_new_comments'),
    # url(r'^retrieve_comments/$', views.get_comments, name='retrieve_comments'),
]
