from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth

from .models import Member
from .forms import SignupForm

# Create your views here.

# 로그인
def log_in(request):
    return render(request, 'account/log_in.html', {})

# 이메일 주소와 비밀번호가 일치하는지 검증
def login_check(request):
    if request.method == "POST":
        if Member.objects.raw("SELECT * FROM 'account_member' WHERE email='%s' AND password='%s'" %(request.POST["email"], request.POST["password"])):
            user = Member.objects.filter(email=request.POST["email"])
            # 로그인 유지 세션
            if request.POST.get("keep_login", False):
                request.session['user'] = user
                # return render(request, 'board_list.html', {'user': user})
                return redirect('board/')
            else:
                
                # return render(request, 'board_list.html', {'user': user})
                return redirect('board/')
        else:
            alert="이메일이나 비밀번호가 맞지 않습니다."
            return render(request, 'account/log_in.html', {'alert': alert})

# 회원가입
def sign_up(request):
    signupform = SignupForm()
    return render(request, 'account/sign_up.html', {'signupform': signupform})

# 중복된 값이 있는지 검증
def signup_check(request):
    if request.method == "POST":
        signupform = SignupForm(request.POST)
        # 이메일 검증
        if Member.objects.raw("SELECT * FROM 'account_member' WHERE email='%s'" % request.POST["email"]):
            alert="중복된 이메일 입니다."
            return render(request, 'account/sign_up.html', {'alert': alert, 'signupform': signupform})
        
        # 닉네임 검증
        elif Member.objects.raw("SELECT * FROM 'account_member' WHERE nickname='{}'".format(request.POST["nickname"])):
            alert="중복된 닉네임 입니다.."
            return render(request, 'account/sign_up.html', {'alert': alert, 'signupform': signupform})
        
        # 휴대폰번호 검증
        elif Member.objects.raw("SELECT * FROM 'account_member' WHERE phone='{}'".format(request.POST["phone"])):
            alert="중복된 휴대폰 번호 입니다."
            return render(request, 'account/sign_up.html', {'alert': alert, 'signupform': signupform})
        
        else:
            member = signupform.save(commit=False)
            member.save()

            alert="회원 가입이 완료되었습니다."
            return render(request, 'account/log_in.html', {'alert': alert})

            


