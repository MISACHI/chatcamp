from django import forms
from user_messages.models import UserMessages


class MessagesForm(forms.ModelForm):
    username = forms.CharField(
        label="Mate",
        widget=forms.TimeInput(attrs={
            "class": "form-control",
            "placeholder": "Enter user to send Message to",
            "name": "user"
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
        fields = ["username", "message"]
