from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from Trial_app.forms import ProfileForm


def index(request):
    return render(request, 'Trial_app/index.html', {})


def home(request):
    return render(request, 'Trial_app/home.html', {})


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