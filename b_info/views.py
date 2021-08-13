from django.shortcuts import render, redirect
from .models import Circle, CircleMember
from b_signup.models import User
from b_apply.models import Apply, Question
from django.utils import timezone
from b_bulletin.models import PromotionPost
from datetime import datetime

# Create your views here.
def info(request):
    #홍보글 리스트
    posts = PromotionPost.objects.all()
    return render(request, "info.html",{'posts':posts})

def regist(request):
    if request.method == "POST":
        title = request.POST['title']
        recruitStartDate = request.POST['recruitStartDate']
        # StartDatetemp = datetime.strptime(recruitStartDate, "%Y-%m-%d %H:%M:%S").date()
        StartDatetemp = datetime.strptime(recruitStartDate, "%Y-%m-%d").date()
        print(StartDatetemp)
        recruitEndDate = request.POST['recruitEndDate']
        #EndDatetemp = datetime.strftime(recruitEndDate, "%Y-%m-%d %H:%M:%S")
        print(recruitEndDate)
        howManyMember = request.POST['howManyMember']
        keyword = request.POST['keyword']
        detailContent = request.POST['detailContent']

        #질문 최대 3개
        count = request.POST['count']
        
        applylist = []
        for i in range(int(count)):
            applylist.append(request.POST['apply%d'%(i+1)])
        print(applylist)

        # img = request.FILES.get('img').name # 파일임 파일이름 구분해야함
        # print(img)
        order = request.POST['order'] #동아리이름
                
        promotionPost = PromotionPost()
        promotionPost.title = title
        promotionPost.recruitStartDate = recruitStartDate
        promotionPost.recruitEndDate = recruitEndDate
        promotionPost.howManyMember = howManyMember
        promotionPost.keyword = keyword
        promotionPost.detailContent = detailContent
        # promotionPost.img = img

        #User 정보 가져오기
        id = request.session['login_ID']
        user = User.objects.get(login_ID = id)

        #동아리 이름 받아와야함
        circle = Circle.objects.get(name = order)
        
        promotionPost.circleID = circle
        promotionPost.userID = user
        promotionPost.writeDate = timezone.now()
        promotionPost.view = 0 #조회수

        promotionPost.save()


        for i in range(int(count)):
            question = Question()
            question.promotionPostID = promotionPost
            question.question = applylist[i]
            question.save()
        

        return redirect('/main_yes')
    else:
        #동아리 부회장, 회장일때 선택할 수 있어야 함
        id = request.session['login_ID']
        user = User.objects.get(login_ID = id)

        circlelist = CircleMember.objects.filter(userID = user)

        #circlelist가 없을경우 예외처리 필요
    
        return render(request, "regist.html", {'circlelist': circlelist})

def circle_register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        introduction = request.POST.get('Introduction')
        topic = request.POST.get('topic')

        create_date = timezone.now()
        
        circle = Circle()
        circle.name = name
        circle.madeDate = create_date
        circle.Introduction = introduction
        circle.topic = topic
        circle.save()

        id = request.session['login_ID']
        user = User.objects.get(login_ID = id)
        circlemember = CircleMember()
        circlemember.circleID = circle
        circlemember.userID = user
        circlemember.position = 3 #3 회장
        circlemember.signupDate = create_date
        circlemember.save()
        
        return redirect('/main_yes')
    else:
        return render(request, "circle_register.html")


