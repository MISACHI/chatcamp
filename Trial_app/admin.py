from django.contrib import admin
from Trial_app.models import(
        Profile,
        Message,
        Notification,
        Feed,
        Friend,
        Comment,
    )

admin.site.register(Profile)
admin.site.register(Message)
admin.site.register(Notification)
admin.site.register(Feed)
admin.site.register(Friend)
admin.site.register(Comment)


