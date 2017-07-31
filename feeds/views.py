from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator

from feeds.forms import FeedsForm, CommentForm
from feeds.models import Feed, Comments


@login_required(login_url='login')
def get_comments(request):
    user = request.user


@login_required(login_url='login')
@transaction.atomic
def feeds(request):
    user = request.user
    feed_data = Feed.get_feeds()
    result = []
    if request.method == 'POST' and user.is_authenticated:
        feeds_form = FeedsForm(request.POST)
        comments_form = CommentForm(request.POST)

        if feeds_form.is_valid() or comments_form.is_valid():
            feed_id = feeds_form.cleaned_data.get('posts')
            if feed_id is not None:
                Feed.objects.create(posts=feed_id, user=user)

            feed_id = request.POST.get('feed_pk')
            comment_data = Comments.get_comments(feed_id)
            print(comment_data)
            result.append(comment_data)
            # print(result)

            user_comments = comments_form.cleaned_data.get('comment')
            Comments.create_new_comment(feed_id, user_comments)
            return redirect('/feeds/')
        else:
            return render(request, 'feeds/feeds.html', {'forms': feeds_form})
    else:
        feeds_form = FeedsForm()
        comments_form = CommentForm()
    # print('result is %s' % result)
    return render(request, 'feeds/feeds.html', {
        'user': user,
        'feeds': feed_data,
        'forms': feeds_form,
        'comments_form': comments_form,
        'comments': result
    })


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
