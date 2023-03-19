import logging

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from profiles.forms import RegisterForm
from profiles.forms import UserForm

logger = logging.getLogger(__name__)


def profiles(request):
    if request.GET.get("param"):
        logger.info(f"My param = {request.GET.get('param')}")
    return HttpResponse("Profiles view")


def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create()
            logger.info(f"User email: {form.cleaned_data['email']}")
            logger.info(f"User password: {form.cleaned_data['password']}")
            return redirect("index")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})

def user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            User.objects.create()
            logger.info(f"User email: {form.cleaned_data['email']}")
            logger.info(f"User password: {form.cleaned_data['password']}")
            return redirect("index")
    else:
        form = UserForm()
    return render(request, "user.html", {"form": form})