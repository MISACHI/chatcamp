from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def user_messages(request):
    return render(request, 'Trial_app/message.html', {})
