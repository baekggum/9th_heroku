from django.shortcuts import render
from b_apply.models import Apply
from b_signup.models import User

# Create your views here.
def mypage(request):
    login_id = request.session.get('login_ID')
    user = User.objects.get(login_ID = login_id)
    

    applys = Apply.objects.filter(userID = user.id)
    print(applys)
    return render(request, "mypage.html", {'applys':applys})

def applySit(request):
    return render(request, "applySit.html")

# def changeProfile(request):
#     return render(request, "changeProfile.html")

# def changePwd1(request):
#     return render(request, "changePwd1.html")

# def changePwd2(request):
#     return render(request, "changePwd2.html")

# def excitingSec(request):
#     return render(request, "excitingSec.html")

# def extraSave(request):
#     return render(request, "extraSave.html")

# def lastLook(request):
#     return render(request, "lastLook.html")

# def myCommnet(request):
#     return render(request, "myComment.html")

# def myGroup(request):
#     return render(request, "myGroup.html")

# def myWrite(request):
#     return render(request, "myWrite.html")