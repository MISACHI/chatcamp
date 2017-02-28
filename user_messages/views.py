from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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


# displays user messages
@login_required(login_url="login")
def user_messages(request):
    current_user = request.user
    msg_from_user = UserMessages.get_sent_messages(current_user)
    msg_data = UserMessages.get_received_messages(current_user)
    return render(request, "user_messages/message.html", {
        "msg_data": msg_data,
        "current_user": current_user,
        "msg_from_user": msg_from_user,
    })
