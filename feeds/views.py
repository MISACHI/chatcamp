from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.core.paginator import Paginator
from django.http import HttpResponse

from feeds.forms import FeedsForm, CommentForm
from feeds.models import Feed, Comments


@login_required(login_url='login')
@transaction.atomic
def feeds(request):
    user = request.user
    feed_data = Feed.get_feeds(user)
    result = []

    for datum in feed_data:
        comment_data = Comments.get_comments(datum.feeds_id)
        feed_list = [datum, comment_data]
        result.append(feed_list)

    if request.method == 'POST' and user.is_authenticated:
        feeds_form = FeedsForm(request.POST)

        if feeds_form.is_valid():
            feed = feeds_form.cleaned_data.get('posts')
            Feed.objects.create(posts=feed, user=user)
            return redirect('/feeds/')
        else:
            return render(request, 'feeds/feeds.html', {'forms': feeds_form})
    else:
        feeds_form = FeedsForm()
        comments_form = CommentForm()
    return render(request, 'feeds/feeds.html', {
        'user': user,
        'feeds': result,
        'forms': feeds_form,
        'comments_form': comments_form,
    })


@login_required(login_url='login')
def comment(request):
    user = request.user
    feed_id = request.POST.get('feed_pk')
    if request.method == 'POST' and user.is_authenticated:
        comments_form = CommentForm(request.POST)
        if comments_form.is_valid():
            user_comments = comments_form.cleaned_data.get('comment')
            Comments.create_new_comment(feed_id, user_comments)
            return redirect('/feeds/')
        else:
            return render(request, 'feeds/save_comments.html', {'comments_form': comments_form})
    else:
        comments_form = CommentForm()
    return render(request, 'feeds/save_comments.html', {'comments_form': comments_form})


# @login_required(login_url='login')
# def get_comments(request):
#     feed_id = request.POST.get('feed_pk')
#     comment_data = Comments.get_comments(feed_id)
#     return render(request, 'feeds/retrieve_comments.html', {'comments': comment_data})


@login_required(login_url='login')
def post_feeds(request):
    user = request.user
    if request.method == 'POST':
        feeds_form = FeedsForm(request.POST)
        if feeds_form.is_valid():
            feed_id = feeds_form.cleaned_data.get('posts')
            Feed.objects.create(posts=feed_id, user=user)
            return redirect('/feeds/')
        else:
            return render(request, 'feeds/post_feeds.html', {'forms': feeds_form})
    else:
        feeds_form = FeedsForm()
    return render(request, 'feeds/post_feeds.html', {
        'forms': feeds_form,
        'user': user,
    })
