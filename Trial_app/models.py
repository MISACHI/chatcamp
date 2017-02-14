from django.db import models
# from authentication.models import Registration
#
#
# class Notification(models.Model):
#     notification_id = models.AutoField(primary_key=True)
#     notifications = models.CharField(max_length=20)
#
#
# class Friend(models.Model):
#     friends_id = models.AutoField(primary_key=True)
#     # user_one = models.ForeignKey(Registration, on_delete=models.CASCADE)
#     user_friend = models.ForeignKey(Registration)
#
#
# class Message(models.Model):
#     message_id = models.AutoField(primary_key=True)
#     message = models.CharField(max_length=200)
#
#
# class Comment(models.Model):
#     comment_id = models.AutoField(primary_key=True)
#     comment = models.CharField(max_length=300)
#     time_posted = models.TimeField()
#
#     def __str__(self):
#         return self.comment + '\n' + self.time_posted
