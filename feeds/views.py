from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def feeds(request):
    # if request.method == 'POST':
    return render(request, 'Trial_app/feeds.html', {})
