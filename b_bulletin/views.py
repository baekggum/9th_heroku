from b_signup.models import User
from b_info.models import Circle
from b_bulletin.models import PromotionPost
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def bulletin(request):
    return render(request, "bulletin.html")


# 모집공고 생성
def create_promo_post(request):
    # 동아리이름과, 유저이름은 절대 입력받지않고, 로그인정보에 담긴 정보를 프론트에서 그대로 보낼것
    # 근데 사용자의 동아리 가입정보를 프론트에서 가지고있어야하는데, CircleMember 모델이 User를 외례키로 사용하고있고
    # 또 CircleMember는 Circle을 외례키로 사용하기떄문에, 두다리 걸쳐서 유저가 속해있는 동아리 객체를 받아올수있다.
    # 그렇게해서 nickName & circle_name을 무결성을 유지해서 보낼 수 있도록 부가적인 작업을 프론트와 백 둘다 해주어야한다.
    circle_name = Circle.objects.get(name=request.POST.get('circlename'))
    nickName = User.objects.get(nickName=request.POST.get('nickName'))
    if not circle_name and not nickName:
        post = PromotionPost()
        post.title = request.POST.get('title')
        post.recruitStartDate = request.POST.get('recruitStartDate')
        post.recruitEndDate = request.POST.get('recruitEndDate')
        post.howManyMember = request.POST.get('howManyMember')
        post.keyword = request.POST.get('keyword')
        post.detailContent = request.POST.get('detailContent')
        post.img = request.POST.get('img')
        post.circleID = circle_name
        post.userID = nickName
        post.save()
    # 그리고 지금 save()에서 반환값이 없기때문에, 성공여부를 구분하기가 어렵다... 조금더 생각해보자
    return HttpResponse('success')


# 모집공고 삭제
def remove_promo_post(request, promo_id):
    # pk값 query변수로 넘겨서 삭제하기
    post = PromotionPost.objects.get(pk=promo_id)
    post.delete()
    return HttpResponse('remove done :)')

