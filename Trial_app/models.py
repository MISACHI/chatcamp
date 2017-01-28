from django.contrib.auth.models import User
from django.db import models


# class Registration(models.Model):
#     app_user_id = models.AutoField(primary_key=True)
#     user = models.OneToOneField(User)
#
#     def __str__(self):
#         return self.user.first_name + '\t\t' + self.user.last_name


class Registration(models.Model):
    app_user_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.first_name + '\t' + self.user.last_name


class Profile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    # profile_pic = models.ImageField()
    app_user_id = models.ForeignKey(Registration, on_delete=models.CASCADE)
    contacts = models.TextField(max_length=10)
    date_of_birth = models.DateField()
    skills = models.CharField(max_length=500)
    profession = models.TextField(max_length=100)
    brief_description = models.CharField(max_length=500)

    def __str__(self):
        return self.date_of_birth + '\n' + self.contacts


class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    notifications = models.CharField(max_length=20)


class Friend(models.Model):
    friends_id = models.AutoField(primary_key=True)
    # user_one = models.ForeignKey(Registration, on_delete=models.CASCADE)
    user_friend = models.ForeignKey(Registration)


class Feed(models.Model):
    feeds_id = models.AutoField(primary_key=True)
    feeds = models.CharField(max_length=200)
    time_posted = models.TimeField()

    def __str__(self):
        return self.feeds + '\n' + self.time_posted


class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=200)


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=300)
    time_posted = models.TimeField()

    def __str__(self):
        return self.comment + '\n' + self.time_posted


# class Posts(models.Model):
#     app_user_id = models.ForeignKey(Registration, on_delete=models.CASCADE)
#     feeds_id = models.ForeignKey(Feed, on_delete=models.CASCADE)
#     comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
#     time_posted = models.TimeField()
#
#     # def __str__(self):
#     #      return self.user.username + '\n' + self.comment
#
#
# class Creates(models.Model):
#     app_user_id = models.ForeignKey(Registration, on_delete=models.CASCADE)
#     profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     data_created = models.DateField
#
#
# class ShootsMessage(models.Model):
#     app_user_id = models.ForeignKey(Registration, on_delete=models.CASCADE)
#     message_id = models.ForeignKey(Message, on_delete=models.CASCADE)
#     time_sent = models.TimeField()