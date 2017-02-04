from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from authentication.forms import RegistrationForm


def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data.get('username')
            email = user_form.cleaned_data.get('email')
            password = user_form.cleaned_data.get('password')

            User.objects.create_user(
                username=username,
                email=email,
                password=password,
            )
            return HttpResponseRedirect('/feeds/')
        else:
            return render(request, 'Trial_app/register.html', {'form': user_form})
    else:
        user_form = RegistrationForm()

    return render(request, 'authentication/register.html', {'form': user_form})

