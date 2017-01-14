from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required

from Trial_app.models import Registration
from Trial_app.forms import LoginForm, RegistrationForm


def index(request):
    return render(request, 'Trial_app/index.html', {})


def home(request):
    return render(request,'Trial_app/home.html', {})


@login_required(login_url='login')
def feeds(request):
    return render(request,'Trial_app/feeds.html', {})


@login_required(login_url='login')
def profile(request):
    return render(request, 'Trial_app/profile.html', {})


# def register(request):
#     if request.method == "POST":
#         user_details = RegistrationForm(request.POST)
#         if user_details.is_valid():
#             form = user_details.save(commit=False)
#             form.set_password(form.password)
#             form.save()
#             return HttpResponseRedirect('/trial/')
#         else:
#             return render(request, 'Trial_app/register.html', {'form' : user_details})
#     else:
#         user_details = RegistrationForm()
#
#     return render(request, 'Trial_app/register.html', {'form' : user_details})

def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/trial/')
        else:
            return render(request, 'Trial_app/register.html', {'form' : user_form})
    else:
        user_form = RegistrationForm()

    return render(request, 'Trial_app/register.html', {'form' : user_form})

# def login(request):
#     if request.method == 'POST':
#         login_form_details = LoginForm(request.POST)
#         if login_form_details.is_valid:
#             email  = request.POST['email']
#             password  = request.POST['password']
#             # login_email = Registration.objects.get(email=email)
#             # login_password = Registration.objects.get(email=email)
#             #
#             # if login_email and login_password:
#
#
# def logout(request):
#     return HttpResponse('You are logged out')

