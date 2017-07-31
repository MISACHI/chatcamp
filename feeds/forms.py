from django import forms
from feeds.models import Feed, Comments


class FeedsForm(forms.ModelForm):
    posts = forms.CharField(
        # label = '',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Post something',
            'name': 'posts',
            'rows': 5,
            'cols': 30,
        }),
    )

    class Meta:
        model = Feed
        fields = ['posts']


class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Post something',
            'name': 'comment',
            'rows': 5,
            'cols': 15,
        }),
    )

    class Meta:
        model = Comments
        fields = ['comment']
