import logging

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate

from profiles.forms import RegisterForm, LoginForm
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
            user = User(
                email=form.cleaned_data["email"],
                username=form.cleaned_data["email"],
            )
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("login")
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

def login_view(request):
   if request.method == "POST":
       form = LoginForm(request.POST)
       if form.is_valid():
           user = authenticate(
               request=request,
               username=form.cleaned_data["email"],
               password=form.cleaned_data["password"],
           )
           if user is None:
               return HttpResponse('BadRequest', status=400)
           login(request, user)
           return redirect("index")
   else:
       form = LoginForm()
   return render(request, "login.html", {"form": form})

def logout_view(request):
   logout(request)
   return redirect("index")