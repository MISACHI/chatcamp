from __future__ import unicode_literals
import uuid

from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


def upload_location(obj, filename):
    return "{0}/{1}".format(obj.profile_id, filename)


@python_2_unicode_compatible
class Profile(models.Model):
    profile_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    profile_pic = models.ImageField(
        upload_to=upload_location,
        null=True, blank=True,
        height_field="height_field",
        width_field="width_field"
    )
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    app_user = models.OneToOneField(User)
    contacts = models.TextField(max_length=10)
    date_of_birth = models.DateField()
    skills = models.CharField(max_length=500)
    profession = models.TextField(max_length=100)
    brief_description = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True, null=True)
    time_updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return '{0} {1}'.format(self.app_user.first_name, self.app_user.last_name)

