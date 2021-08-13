from django.shortcuts import render
from b_bulletin.models import PromotionPost
from .models import Apply, Question

# Create your views here.
def apply(request,postid):
    post = PromotionPost.objects.get(pk=postid)
    questionlist = Question.objects.filter(promotionPostID = post)
    
    return render(request, "apply.html",{'post':post, 'questionlist': questionlist})

def newApply(request):

    newApply = Apply()
    newApply.promotionPostID = request.POST.get('promotionPostID')
    newApply.questionID = request.POST.get('questionID')
    newApply.userID = request.POST.get('userID')
    newApply.answer = request.POST.get('answer')
    newApply.temporary = request.POST.get('temporary')
    newApply.save()

    return render(request,'info.html')