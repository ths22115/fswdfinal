import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import User, Task

# Create your views here.
# task.objects.filter(done=false)
# task.objects.all()
#
# tasks = task.objects.all()
# done_tasks = tasks.filter(done=True)
# model mail?

def index(request): #done

    # Authenticated users view their list page
    if request.user.is_authenticated:
        return render(request, "todolist/inbox.html")

    # Everyone else is prompted to sign in
    else:
        return HttpResponseRedirect(reverse("login"))


@login_required
def page(request, page): #done
    # Filter tasks returned based on page
    if page == "list":
        tasks = Task.objects.filter(
            user=request.user, done=False
        )
    elif page == "finished":
        tasks = Task.objects.filter(
            user=request.user, done=True
        )
    else:
        return JsonResponse({"error": "Invalid mailbox."}, status=400)

    # Return emails in reverse chronologial order
    tasks = tasks.order_by("timestamp").all()
    return JsonResponse([task.serialize() for task in tasks], safe=False)

def login_view(request): #done
    if request.method == "POST":

        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "todolist/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "todolist/login.html")


def logout_view(request): #done
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request): #done
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "todolist/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(
                name,
                first_name=name,
                email=email,
                password=password,
            )
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "todolist/register.html", {
                "message": "Email address already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "todolist/register.html")