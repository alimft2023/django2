from django.shortcuts import render
from .models import User, UserProfile


# Create your views here.
def login(request):
    return render(request, "accounts/login.html", {})


def register(request):
    return render(request, "accounts/register.html", {})


def addeducation(request):
    return render(request, "accounts/add-education.html", {})


def addexperience(request):
    return render(request, "accounts/add-experience.html", {})


def createprofile(request):
    return render(request, "accounts/create-profile.html", {})


def dashboard(request):
    return render(request, "accounts/dashboard.html", {})


def profile(request, pk):
    user_profile = UserProfile.objects.get(pk=pk)
    return render(request, "accounts/profile.html", {"user_profile": user_profile})


def profiles(request):
    return render(request, "accounts/profiles.html", {})
