from __future__ import unicode_literals
import uuid
from datetime import date

from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

from user_profile.models import Profile


@python_2_unicode_compatible
class Feed(models.Model):
    feeds_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User)
    profile = models.ForeignKey(Profile, null=True)
    posts = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.posts)

    @staticmethod
    def get_user_feeds(feed_data=None):  # function is a static method gets user feeds and can be called on the class
        if feed_data is not None:
            feeds = Feed.objects.filter(created__lte=feed_data)
        else:
            feeds = Feed.objects.filter(created__lte=date.today())
        return feeds

    @staticmethod
    def get_feeds():
        feeds = Feed.objects.all()
        return feeds

    class Meta:
        ordering = ["-created", "-time_updated"]


@python_2_unicode_compatible
class Comments(models.Model):
    comment_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    comment = models.CharField(max_length=200)
    feed = models.ForeignKey(Feed)
    created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0} {1}'.format(self.feed, self.comment)

    @staticmethod
    def create_new_comment(feed_id, comment):
        # feed = Feed.objects.get(feeds_id=feed_id)
        Comments.objects.create(feed_id=feed_id, comment=comment)

    @staticmethod
    def get_comments(feed_id):
        comments = Comments.objects.filter(feed_id=feed_id)
        return comments

    class Meta:
        ordering = ["-created", "-time_updated"]
