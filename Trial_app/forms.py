from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from Trial_app.models import Profile


# class RegistrationForm(forms.ModelForm):
#     password2 = forms.CharField(
#         label = 'Password confirmation',
#         widget = forms.PasswordInput(attrs={
#             'class' : 'form-control',
#             'placeholder' : 'Confirm password',
#             'name' : 'password2'
#         })
#     )
#
#     def clean(self):
#         password = self.cleaned_data.get('password')
#         password2 = self.cleaned_data.get('password2')
#
#         if not password2:
#             raise forms.ValidationError('You must Confirm Your password')
#
#         if password != password2:
#             raise forms.ValidationError('Your passwords Do not match!')
#             return password2
#
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'username', 'email', 'password', 'password2']
#
#         widgets = {
#             'first_name' : forms.TextInput(
#                 attrs={
#                     'class' : 'form-control',
#                     'placeholder' : 'First name',
#                     'name' : 'first_name',
#                 }
#             ),
#             'last_name' : forms.TextInput(
#                 attrs={
#                     'class' : 'form-control',
#                     'placeholder' : 'Last name',
#                     'name' : 'last_name',
#                 }
#             ),
#             'username' : forms.TextInput(
#                 attrs={
#                     'class' : 'form-control',
#                     'placeholder' : 'Username',
#                     'name' : 'username',
#                 }
#             ),
#             'email' : forms.EmailInput(
#                 attrs={
#                     'class' : 'form-control',
#                     'placeholder' : 'Email',
#                     'name' : 'email',
#                 }
#             ),
#             'password' : forms.PasswordInput(
#                 attrs={
#                     'class' : 'form-control',
#                     'placeholder' : 'password',
#                     'name' : 'password',
#                 }
#             ),
#
#         }

class RegistrationForm(forms.ModelForm):
    confirmpassword = forms.CharField(
    label = 'Password Confirmation',
    widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Confirm password',
        'name':'confirmpassword',
    }),
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
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'confirmpassword']
        widgets = {
            'username':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Username',
                'name' : 'username',
            }),
            'email':forms.EmailInput(attrs={
                'class':'form-control',
                'placeholder':'Email address',
                'name' : 'email',
            }),
            'first_name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'First name here',
                'name' : 'first_name',
            }),
            'last_name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Last name here',
                'name' : 'last_name',
            }),
            'password':forms.PasswordInput(attrs={
                'class':'form-control',
                'placeholder':'Password',
                'name':'password',
            }),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label = 'Username',
        widget = forms.TextInput(
            attrs = {
                'class' : 'form-control',
                'placeholder' : 'Username',
                'name' : 'username',
            }
        )
    )
    password = forms.CharField(
        label = 'Password',
        widget = forms.PasswordInput(
            attrs = {
                'class' : 'form-control',
                'placeholder' : 'Password',
                'name' : 'password',
            }
        )
    )


class ProfileForm(forms.ModelForm):
    dob = forms.DateField(
        label = 'Date of Birth',
        widget = forms.DateInput(
            attrs = {
                'class' : 'form-control',
                'name' : 'dob',
            }
        )
    )
    tel_no = forms.CharField(
        label = 'Mobile number',
        widget = forms.TextInput(
            attrs = {
                'class' : '',
                'name' : 'tel_no',
            }
        )
    )
    prof_pic = forms.FileField(
        label = 'Profile picture',
        widget = forms.FileInput(
            attrs = {
                'class' : 'hidden',
                'name' : 'prof_pic',
            }
        )
    )
    brief_description = forms.CharField(
        label = 'Bio',
        widget = forms.Textarea(
            attrs = {
                'class' : 'form-control',
                'placeholder' : 'Tell about yourself',
                'name' : 'brief_description',
            }
        )
    )
    profession = forms.CharField(
        label = 'Occupation',
        widget = forms.TextInput(
            attrs = {
                'class' : 'form-control',
                'placeholder' : 'Where have you worked?',
                'name' : 'profession',
            }
        )
    )
    skills = forms.CharField(
        label = 'Skills',
        widget = forms.Textarea(
            attrs = {
                'class' : 'form-control',
                'placeholder' : 'Flaunt your skills',
                'name' : 'skills',
            }
        )
    )
    location = forms.CharField(
        label = 'Place or residence',
        widget = forms.TextInput(
            attrs = {
                'class' : 'form-control',
                'placeholder' : 'Where do you live',
                'name' : 'location',
            }
        )
    )

    class Meta:
        model = Profile
        fields = ['dob', 'tel_no', 'prof_pic', 'brief_description', 'profession', 'skills']