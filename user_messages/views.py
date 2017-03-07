from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from user_messages.forms import MessagesForm
from user_messages.models import UserMessages
from django.contrib.auth.models import User


# for displaying message forms
@login_required(login_url="login")
def user_messages_form(request):
    if request.method == "POST":
        messages = MessagesForm(request.POST)
        if messages.is_valid():
            user_from = request.user
            user_to = messages.cleaned_data.get("message_to")
            user_to_obj = User.objects.get(username=user_to)
            user_message = messages.cleaned_data.get("message")

            UserMessages.create_message(user_from, user_to_obj, user_message)
            return redirect("/messages/")
        else:
            return render(request, "user_messages/message_form.html", {
                "messages": messages,
            })
    else:
        messages = MessagesForm()
    return render(request, "user_messages/message_form.html", {
        "messages": messages,
    })


# @require_http_methods(["GET", "POST"])
# @login_required(login_url="login")
# def user_messages(request):
#     current_user = request.user
#     user_to = request.POST.get("message_to")
#     # user_to_obj = User.objects.get(username=user_to)
#     user_message = request.POST.get("message")
#
#     UserMessages.create_message(current_user, user_to, user_message)
#     message_id = UserMessages.objects.filter(user_messages=user_message).values("user_messages_id")
#     msg_to_user = UserMessages.get_sent_messages(message_id)
#     msg_from_user = UserMessages.get_received_messages(current_user)
#
#     return render(request, "user_messages/message.html", {
#         "msg_from_user": msg_from_user,
#         "current_user": current_user,
#         "msg_to_user": msg_to_user,
#     })


# displays user messages
@login_required(login_url="login")
def user_messages(request):
    current_user = request.user
    # unread = UserMessages.get_unread_messages_(current_user)
    msg_to_user = UserMessages.get_sent_messages(current_user)
    msg_from_user = UserMessages.get_received_messages(current_user)

    return render(request, "user_messages/message.html", {
        "msg_from_user": msg_from_user,
        "current_user": current_user,
        "msg_to_user": msg_to_user,
        # "unread": unread,
    })
