from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from Trial_app.forms import RegistrationForm, ProfileForm


def index(request):
    return render(request, 'Trial_app/index.html', {})


def home(request):
    return render(request, 'Trial_app/home.html', {})


def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            user_data = user_form.save(commit=False)
            user_data.set_password(user_data.password)
            user_data.save(commit=True)
            return HttpResponseRedirect('/trial/feeds')
        else:
            return render(request, 'Trial_app/register.html', {'form': user_form})
    else:
        user_form = RegistrationForm()

    return render(request, 'Trial_app/register.html', {'form': user_form})



@login_required(login_url='login')
def feeds(request):
    # if request.method == 'POST':
    return render(request, 'Trial_app/feeds.html', {})


@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        profile_info = ProfileForm(request.POST)
        if profile_info.is_valid():
            profile_info.save(commit=True)
        else:
            return render(request, 'Trial_app/profile.html', {'form': profile_info})
    else:
        profile_info = ProfileForm()
    return render(request, 'Trial_app/profile.html', {'form': profile_info})


@login_required(login_url='login')
def message(request):
    return render(request, 'Trial_app/message.html', {})