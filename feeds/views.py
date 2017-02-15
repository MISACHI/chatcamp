from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from feeds.forms import FeedsForm
from django.contrib.auth.models import User
from authentication.models import Registration
from feeds.models import Feed


@login_required(login_url='login')
def feeds(request):
    user = request.user
    feed_data = Feed.get_user_feeds()
    # feed_data = Feed()
    # feed_data.user = user
    # posts = request.POST['posts']
    # feed_data.posts = posts
    # feed_data.save()
    # # if request.method == 'POST':
    # #     feeds_form = FeedsForm(request.POST)
    # #     if feeds_form.is_valid():
    # #         user_posts = feeds_form.cleaned_data['posts']
    # #         Feed.objects.create(posts=user_posts)
    # #     else:
    # #         return render(request, 'feeds/feeds.html', {'forms': feeds_form})
    # # else:
    # #     return FeedsForm()
    return render(request, 'feeds/feeds.html', {
        'user' : user,
        'feeds' : feed_data,
    })


@login_required(login_url='login')
def post_feeds(request):
    user = request.user
    if request.method == 'POST':
        feeds_form = FeedsForm(request.POST)
        if feeds_form.is_valid():
            user_posts = feeds_form.cleaned_data.get('posts')
            Feed.objects.create(posts=user_posts, user=user)
            return redirect('/feeds/')
        else:
            return render(request, 'feeds/post_feeds.html', {'forms': feeds_form})
    else:
        feeds_form = FeedsForm()
    return render(request, 'feeds/post_feeds.html', {
        'forms': feeds_form,
        'user' : user,
    })
