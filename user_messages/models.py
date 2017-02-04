from django.db import models
from authentication.models import Registration


class UserMessages(models.Model):
    user_messages_id = models.AutoField(primary_key=True)
    app_user_id = models.ForeignKey(Registration)
    user_messages = models.CharField(max_length=500)
    user_messages_time = models.TimeField()
