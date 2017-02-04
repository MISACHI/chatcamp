from django.db import models
from authentication.models import Registration


class Feed(models.Model):
    feeds_id = models.AutoField(primary_key=True)
    user_feed = models.ForeignKey(Registration)
    feeds = models.CharField(max_length=200)
    time_posted = models.TimeField()

    def __str__(self):
        return self.feeds + '\n' + self.time_posted
