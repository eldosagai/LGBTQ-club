from unicodedata import name
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User

# Create your views here.
def gayshouse(request):
    return render(request,'main.html')

def log_in(request):
    return render(request,'log_in.html')

def sign_up(request):
    if request.method == "POST":
        data=request.POST # d stands for data perv
        email = data['email']
        username = data['username']
        name = data['name']
        surname = data['surname']
        password = data['password']
        User.objects.create_user(
            username = username, password = password, email = email,
            name = name, surname = surname)
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect (request,'log_in')
    return render(request,'sign_up.html')
    # def log_in(request):
    # form = Log_inForm()
    # print(request.method)
    # if request.method == "POST":
    #     form = Log_inForm(request.POST)
    #     if not form.is_valid():
    #         username = request.POST['username']
    #         password = request.POST['password']
    #         user = authenticate(username=username, password=password)
    #         if user is not None:
    #             login(request, user)
    #             return render (request, "home.html")
    #         else:
    #             return render (request, "log_in.html", {"form": form, "error": "Wrong username or password"})
    # return render(request, "log_in.html", {"form": form})

