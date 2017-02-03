from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from Trial_app.models import Profile


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            'name':'username',
        }),
        max_length=30,
        required=True,
        help_text='Usernames may contain <strong>alphanumeric</strong>, <strong>_</strong> and <strong>.</strong> characters'
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email address',
            'name': 'email',
        }),
        required=True,
        max_length=75

    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'name': 'password',
        })
    )
    confirmpassword = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm password',
            'name': 'confirmpassword',
        }),
        required=True
    )

    def clean(self):
        password = self.cleaned_data.get('password')
        confirmpassword = self.cleaned_data.get('confirmpassword')

        if not confirmpassword:
            raise forms.ValidationError('You must Confirm Your password')

        if password != confirmpassword:
            raise forms.ValidationError('Your passwords Do not match!')
            return confirmpassword

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirmpassword']
        # widgets = {
        #     'username': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Username',
        #         'name': 'username',
        #     }),
        #     'email': forms.EmailInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Email address',
        #         'name': 'email',
        #     }),
        #     'first_name': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'First name here',
        #         'name': 'first_name',
        #     }),
        #     'last_name': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Last name here',
        #         'name': 'last_name',
        #     }),
        #     'password': forms.PasswordInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Password',
        #         'name': 'password',
        #     }),
        # }


class LoginForm(AuthenticationForm):
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
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'name': 'password',
            }
        )
    )


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
    day = forms.DateField(
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
                'placeholder' : 'Mobile Number',
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
    location = forms.CharField(
        label='Place or residence',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Where do you live',
                'name': 'location',
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
            'day',
            'tel_no',
            'prof_pic',
            'brief_description',
            'profession',
            'skills',
        ]
