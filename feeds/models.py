from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Feed(models.Model):
    feeds_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    posts = models.CharField(max_length=200, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return str(self.feeds_id) + '\t' + str(self.time_updated) + '\t' + str(self.timestamp) + '\n' + self.posts
