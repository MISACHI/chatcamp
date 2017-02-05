from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from feeds.forms import FeedsForm
from feeds.models import Feed


@login_required(login_url='login')
def feeds(request):
    if request.method == 'POST':
        feeds_form = FeedsForm(request.POST)
        if feeds_form.is_valid():
            posts = feeds_form.cleaned_data.get('posts', None)
            Feed.objects.create(posts=posts)
        else:
            return render(request, 'feeds/feeds.html', {'forms': feeds_form})
    else:
        return FeedsForm()
    return render(request, 'feeds/feeds.html', {'forms': feeds_form})