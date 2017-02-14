from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Profile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    profile_pic = models.ImageField(null=True)
    app_user_id = models.OneToOneField(User)
    contacts = models.TextField(max_length=10)
    date_of_birth = models.DateField()
    skills = models.CharField(max_length=500)
    profession = models.TextField(max_length=100)
    brief_description = models.CharField(max_length=500)

    def __str__(self):
        return self.date_of_birth + '\n' + self.contacts