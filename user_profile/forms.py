from django import forms
from user_profile.models import Profile


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        label='First name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'First name',
                'name': 'first_name',
            }
        )
    )
    last_name = forms.CharField(
        label='Last name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Last name',
                'name': 'last_name',
            }
        )
    )
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username',
                'name': 'username',
            }
        )
    )
    email = forms.EmailField(
        label='Email address',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email address',
                'name': 'email',
            }
        )
    )
    birth_date = forms.DateField(
        label='Date of Birth',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'name': 'dob',
            }
        )
    )
    tel_no = forms.CharField(
        label='Mobile number',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Mobile Number',
                'name': 'tel_no',
            }
        )
    )
    prof_pic = forms.FileField(
        label='Profile picture',
        widget=forms.FileInput(
            attrs={
                'class': 'hidden',
                'name': 'prof_pic',
            }
        )
    )
    brief_description = forms.CharField(
        label='Bio',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Tell about yourself',
                'name': 'brief_description',
            }
        )
    )
    profession = forms.CharField(
        label='Occupation',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Where have you worked?',
                'name': 'profession',
            }
        )
    )
    skills = forms.CharField(
        label='Skills',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Flaunt your skills',
                'name': 'skills',
            }
        )
    )

    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'birth_date',
            'tel_no',
            'prof_pic',
            'brief_description',
            'profession',
            'skills',
        ]
