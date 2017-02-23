from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class UserMessages(models.Model):
    user_messages_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    user_messages = models.CharField(max_length=500)
    user_messages_time = models.TimeField()

    def __str__(self):
    	return self.user + self.user_messages + self.user_messages_time
