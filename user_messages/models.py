from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class UserMessages(models.Model):
    user_messages_id = models.AutoField(primary_key=True)
    user_from = models.CharField(max_length=50)
    user_to = models.ForeignKey(User)
    user_messages = models.CharField(max_length=500)
    user_messages_timestamp = models.TimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.user + self.user_messages + self.user_messages_timestamp

    @staticmethod
    def get_user_messages(user):
        message_data = UserMessages.objects.filter(user=user)
        return message_data
