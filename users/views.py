from django.http import HttpResponse
from django.shortcuts import render
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
        )
        return HttpResponse("signup post로 요청중")


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
            return HttpResponse("로그인 성공")
        else:
            return HttpResponse("로그인 실패")
