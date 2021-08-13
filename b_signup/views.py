from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.http import HttpResponse
from .models import User, UserInterest
from django.contrib.auth.hashers import make_password
# Create your views here.


def signup1(request):
    if request.method == "POST":
        username = request.POST.get('username',None)
        birth = request.POST.get('birth', None)
        phoneNumber = request.POST.get('phoneNumber', None)

        request.session['signup_username'] = username
        request.session['signup_birth'] = birth
        request.session['signup_phoneNumber'] = phoneNumber
        return redirect('/signup2')
        
    return render(request, "signup1.html")


def signup2(request):
    if 'signup_username' in request.session and 'signup_birth' in request.session and 'signup_phoneNumber' in request.session:
        if request.method == "POST":
            enterYear = request.POST.get('enterYear', None)
            school = request.POST.get('school', None)
            email = request.POST.get('email', None)

            request.session['signup_school'] = school
            request.session['signup_email'] = email
            request.session['signup_enterYear'] = enterYear
            return redirect('/signup3')
        return render(request, "signup2.html")


def signup3(request):
    if 'signup_school' in request.session and 'signup_email' in request.session:
        if request.method == "POST":
            chkAll = request.POST.get('chkAll', None)
            return redirect('/signup4')
        return render(request, "signup3.html")


def signup4(request):
    if 'signup_school' in request.session and 'signup_email' in request.session:
        if request.method=="POST":
            login_ID = request.POST.get('login_ID', None)
            nickName = request.POST.get('nickName', None)
            password = request.POST.get('password', None)
            re_password = request.POST.get('re_password', None)

            res_data = {}
            if password != re_password:
                res_data['error'] = "비밀번호가 다릅니다"

                return render(request, 'signup4.html', res_data)

            culture_art = request.POST.get('culture_art', None)
            volunteer_social = request.POST.get('volunteer_social', None)
            academic_cultivative = request.POST.get('academic_cultivative', None)
            startup_employment = request.POST.get('startup_employment', None)
            language = request.POST.get('language', None)
            physics = request.POST.get('physics', None)
            coding = request.POST.get('coding', None)
            study = request.POST.get('study', None)

            if culture_art == "on":
                culture_art = True
            else:
                culture_art = False
            if volunteer_social == "on":
                volunteer_social = True
            else:
                volunteer_social = False
            if academic_cultivative == "on":
                academic_cultivative = True
            else:
                academic_cultivative = False
            if startup_employment == "on":
                startup_employment = True
            else:
                startup_employment = False
            if language == "on":
                language = True
            else:
                language = False
            if physics == "on":
                physics = True
            else:
                physics = False
            if coding == "on":
                coding = True
            else:
                coding = False
            if study == "on":
                study = True
            else:
                study = False

            username = request.session['signup_username']
            birth = request.session['signup_birth']
            birth = str(birth)
            phoneNumber = request.session['signup_phoneNumber']
            enterYear = request.session['signup_enterYear']
            enterYear = str(enterYear)
            school = request.session['signup_school']
            email = request.session['signup_email']
            print(login_ID)
            print(nickName)
            print(login_ID)
            print(username)
            print(enterYear)
            print(birth)

            user = User(
                login_ID = login_ID,
                nickName = nickName,
                username = username,
                passWord = make_password(password),
                enterYear = enterYear,
                birth = birth,
                school = school,
                email = email
            )
            user.save()

            user_interest = UserInterest(
                user_ID = user,
                culture_art = culture_art,
                volunteer_social = volunteer_social,
                academic_cultivative = academic_cultivative,
                startup_employment = startup_employment,
                language = language,
                physics = physics,
                coding = coding,
                study = study
            )
            user_interest.save()
            return redirect('/signup5')
            
        return render(request, "signup4.html")


def signup5(request):
    return render(request, "signup5.html")


def sendMail(request):

    # 이름 , 생년월일 , emailAuth함수 링크를담은 메일생성
    name = request.GET["username"]
    birth = request.GET['birth']
    link = 'http://localhost:8000/emailauth'
    message_data = f'이름 : {name} 성별 : {birth}\n 위사항이맞다면 링크를 눌러 인증을완료해주세요 \n {link}'
    mail_to = request.GET['email']
    email = EmailMessage('원동력 이메일 인증입니다', message_data, to=[mail_to])

    if email.send() == 1:
        return HttpResponse('메일전송 성공!')
    else:
        return HttpResponse('메일전송 실패!')


def emailAuth(request):
    # 이링크를 접속했다면 인증이완료된것임으로 별도의 동작없이 200 반환
    return HttpResponse('이메일인증 성공!')
