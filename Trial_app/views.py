from django.shortcuts import render


def index(request):
    return render(request, 'Trial_app/index.html', {})


def home(request):
    return render(request, 'Trial_app/home.html', {})