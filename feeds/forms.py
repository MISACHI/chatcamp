from django import forms
from feeds.models import Feed


class FeedsForm(forms.ModelForm):
    posts = forms.CharField(
        # label = '',
        widget = forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Post something',
            'name': 'posts',
        }),
    )

    class Meta:
        model = Feed
        fields = ['posts']
