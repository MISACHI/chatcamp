from __future__ import unicode_literals
import uuid

from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


class UserMessagesManager(models.Manager):
    def read_message(self, message_id):
        result = []
        for _id in message_id:
            message = super(UserMessagesManager, self).get(pk=_id)
            message.is_read = True
            message.save()
            result.append(message)
        return result


@python_2_unicode_compatible
class UserMessages(models.Model):
    objects = UserMessagesManager()
    messages_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user_to = models.ForeignKey(User, related_name='msg_to_user')
    user_from = models.ForeignKey(User, related_name='msg_from_user')
    user_messages = models.CharField(max_length=500)
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0} {1} {2}'.format(str(self.created), self.user_messages, str(self.is_read))

    @staticmethod
    def get_sent_messages(user):
        message_data = UserMessages.objects.filter(user_to=user).values_list('messages_id', flat=True)
        msgs = UserMessages.objects.read_message(message_data)
        return msgs

    @staticmethod
    def get_unread_messages_(user):
        unread_messages = UserMessages.objects.filter(
            Q(user_to=user) &
            Q(is_read=False)
        ).values_list('messages_id', flat=True)
        msgs = UserMessages.objects.read_message(unread_messages)
        return msgs

    @staticmethod
    def get_received_messages(user):
        message_data = UserMessages.objects.filter(user_from=user)
        return message_data

    @staticmethod
    def get_conversation(user):
        conversations = UserMessages.objects.filter(user_to=user)

    @staticmethod
    def create_message(from_user, to_user, message):
        UserMessages.objects.create(
            user_from=from_user,
            user_to=to_user,
            user_messages=message,
        )

    class Meta:
        ordering = ["-created"]
