from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from feeds.models import Feed


@login_required(login_url='login')
def feeds(request):
    if request.method == 'POST':
        feeds_data = request.POST['feeds']
        Feed.objects.create(feeds=feeds_data)
    else:
        return HttpResponse("Only Post Allowed")
    return render(request, 'feeds/feeds.html', {'form': feeds_data})
