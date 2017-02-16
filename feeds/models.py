from __future__ import unicode_literals
from django.db import models
from datetime import date
from django.contrib.auth.models import User
from user_profile.models import Profile
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Feed(models.Model):
    feeds_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    profile = models.ForeignKey(Profile, null=True)
    posts = models.CharField(max_length=200, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return str(self.feeds_id) + '\t' + str(self.time_updated) + '\t' + str(self.timestamp) + '\n' + self.posts

    @staticmethod
    def get_user_feeds(feed_data=None):  # function is a static method gets user feeds and can be called on the class
        if feed_data is not None:
            feeds = Feed.objects.filter(feeds_id__lte=feed_data)
        else:
            feeds = Feed.objects.filter(timestamp__lte=date.today())
        return feeds

    class Meta:
        ordering = ["-timestamp", "-time_updated"]
