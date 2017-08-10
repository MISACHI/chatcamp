from django import forms
from user_messages.models import UserMessages

data = {}
data.


class MessagesForm(forms.ModelForm):
    message_to = forms.CharField(
        label="Message to",
        widget=forms.TimeInput(attrs={
            "class": "form-control",
            "placeholder": "Enter user to send Message to",
            "name": "msg_to"
        })
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Your message",
            "name": "message",
        })
    )

    class Meta:
        model = UserMessages
        fields = ["message_to", "message"]
