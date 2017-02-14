from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from authentication.forms import RegistrationForm
from feeds.models import Feed


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
            user = authenticate(username=username, password=password)
            login(request, user)
            _success_msg = '{0} was successfully added'.format(user.username)
            feed = Feed(user=user, posts=_success_msg)
            feed.save()
            return redirect('/feeds/')
        else:
            return render(request, 'authentication/register.html', {'form': user_form})
    else:
        user_form = RegistrationForm()

    return render(request, 'authentication/register.html', {'form': user_form})

