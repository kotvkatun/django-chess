from django.contrib.auth import authenticate, login, logout
from django.shortcuts import reverse, render
from django.http import HttpResponseRedirect
from django.db import IntegrityError
from .models import User


def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
    else:
        return render(
            request,
            "login.html",
            {"message": "Invalid username and/or password."},
        )


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # Attempt to create new user
        try:
            user = User.objects.create_user(username, password)
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        except IntegrityError:
            return render(
                request,
                "register.html",
                {"message": "Username already taken."},
            )
    return render(request, "register.html")
