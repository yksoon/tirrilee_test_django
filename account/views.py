from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Member

# Create your views here.

def log_in(request):
    return render(request, 'account/log_in.html', {})

def sign_up(request):
    return render(request, 'account/sign_up.html', {})

def signup_check(request):
    if request.method == "POST":
        if Member.objects.raw("SELECT * FROM 'account_member' WHERE email='%s'" % request.POST["email"]):
            return redirect('sign_up')
        
        elif Member.objects.raw("SELECT * FROM 'account_member' WHERE nickname='{}'".format(request.POST["nickname"])):
            return redirect('sign_up')
        
        elif Member.objects.raw("SELECT * FROM 'account_member' WHERE phone='{}'".format(request.POST["phone"])):
            return redirect('sign_up')
        
        else:
            Member.objects.create(email=request.POST["email"], password=request.POST["password"], nickname=request.POST["nickname"], phone=request.POST["phone"])
            user = User(username=request.POST["email"])
            return redirect('log_in')

