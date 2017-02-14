from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Registration(models.Model):
    app_user_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.first_name + '\t' + self.user.last_name