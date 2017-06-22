from django.conf.urls import url
from user_messages.views import user_messages_form, user_messages

urlpatterns = [
    url(r"^$", user_messages, name="trial_messages"),
    url(r'^forms/$', user_messages_form, name="trial_msgform"),
]
