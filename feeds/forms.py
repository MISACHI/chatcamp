from django import forms
from feeds.models import Feed


class FeedsForm(forms.ModelForm):
    posts = forms.CharField(
        label = '',
        widget = forms.Textarea({
            'class': 'form-control',
            'placeholder': 'Post something',
            'name': 'posts',
        })
    )

    class Meta:
        model = Feed
        fields = ['posts']

    def clean(self):
        # cleaned_data = super(FeedsForm, self).clean()
        # posts = cleaned_data.get('posts')
        posts = self.cleaned_data.get('posts',None)
        # do something
        return self.cleaned_data

