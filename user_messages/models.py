from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class UserMessages(models.Model):
    user_messages_id = models.AutoField(primary_key=True)
    user_to = models.ForeignKey(User, related_name='+')
    user_from = models.ForeignKey(User, related_name='+')
    user_messages = models.CharField(max_length=500)
    user_messages_timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return str(self.user_messages_timestamp) + "\t" + self.user_messages

    @staticmethod
    def get_sent_messages(user):
        message_data = UserMessages.objects.filter(user_to=user)
        return message_data

    @staticmethod
    def get_received_messages(user):
        message_data = UserMessages.objects.filter(user_from=user)
        return message_data

    @staticmethod
    def create_message(from_user, to_user, message):
        UserMessages.objects.create(
            user_from=from_user,
            user_to=to_user,
            user_messages=message
        )
