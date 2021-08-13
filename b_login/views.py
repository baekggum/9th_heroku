from django.shortcuts import render, get_object_or_404
from b_signup.models import User, UserInterest
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.contrib.auth import login

# Create your views here.
def login(request):
    if request.method == "POST":
        id = request.POST['ID']
        password = request.POST['password']
        user = get_object_or_404(User, login_ID = id)
        if check_password(password, user.passWord):
            request.session['nickName'] = user.nickName
            request.session['login_ID'] = id
            request.session['school'] = user.school
            # login(request, user)
            return render(request, "main_yes.html")
        else:
            messages.warning(request, "가입하지 않은 아이디이거나, 잘못된 비밀번호입니다.")
            return render(request, "login.html")
    else:
        return render(request, 'login.html')