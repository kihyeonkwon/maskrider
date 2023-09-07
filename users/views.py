from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import User


# Create your views here.
@csrf_exempt
def signup(request):
    print(request.method)
    if request.method == "GET":
        return render(request, "users/signup.html")
    elif request.method == "POST":
        User.objects.create_user(
            username=request.POST["username"],
            email=request.POST["email"],
            password=request.POST["password"],
            image=request.FILES.get("image"),
        )
        return redirect("/users/login/")


def login(request):
    if request.method == "GET":
        return render(request, "users/login.html")
    elif request.method == "POST":
        # 로그인 로직
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("/todos/")
        else:
            return HttpResponse("로그인 실패")


def logout(request):
    if request.method == "POST":
        auth_logout(request)
        return redirect("/todos/")


def profile(request, user_id):
    user = User.objects.get(id=user_id)
    todos = user.todo_set.all()

    context = {"user": user, "todos": todos}
    return render(request, "users/profile.html", context)
