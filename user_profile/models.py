from django.db import models
from authentication.models import Registration


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